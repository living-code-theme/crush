"""Resume a labeled demo in Crush's real themed conversation UI, offline."""
import json
import sqlite3


SESSION = 'a40d1e4c-1150-4000-8000-000000000030'


def prepare(c):
    c.git_fixture()
    c.copy(f'themes/{c.slug}.json', f'.config/crush/themes/{c.slug}.json')
    config = {'options': {'tui': {'active_theme': c.slug}, 'disable_provider_auto_update': True,
                          'disable_metrics': True, 'disable_default_providers': True},
              'providers': {'capture': {'name': 'Local demo (offline)', 'type': 'openai-compat',
                  'base_url': 'http://127.0.0.1:9/v1', 'api_key': 'capture-not-a-real-key',
                  'models': [{'id': 'local-demo', 'name': 'Local demo', 'context_window': 128000, 'default_max_tokens': 4096}]}},
              'models': {'large': {'model': 'local-demo', 'provider': 'capture'},
                         'small': {'model': 'local-demo', 'provider': 'capture'}}}
    c.write('.config/crush/crush.json', json.dumps(config))
    c.env['CRUSH_GLOBAL_CONFIG'] = str(c.home / '.config/crush')
    # Let the pinned application create/migrate its own disposable database first.
    c.run(['crush', 'session', 'list', '--json'])
    c.write('glyph-field/.crush/init', '')
    database = c.work / '.crush/crush.db'
    if not database.is_file():
        raise RuntimeError('Crush did not initialize its local session store')
    timestamp = 1767268800
    with sqlite3.connect(database) as db:
        db.execute('INSERT INTO sessions (id, title, created_at, updated_at) VALUES (?, ?, ?, ?)',
                   (SESSION, 'Glyph field · local demo', timestamp, timestamp))
        for index, role, text in (
            (1, 'user', 'Review the glyph render loop and suggest a safer implementation. (Local demo)'),
            (2, 'assistant', (c.root / 'capture/review.md').read_text()),
        ):
            parts = [{'type': 'text', 'data': {'text': text}}]
            if role == 'assistant':
                parts.append({'type': 'finish', 'data': {'reason': 'end_turn', 'time': timestamp + index}})
            db.execute('''INSERT INTO messages
                (id, session_id, role, parts, model, provider, created_at, updated_at, finished_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                (f'demo-{index}', SESSION, role, json.dumps(parts), 'local-demo', 'capture',
                 timestamp + index, timestamp + index, timestamp + index))
    return ['crush', '--session', SESSION]


def drive(c):
    c.wait_text(r'add boundary tests next|trust this')
    if 'trust' in c.text().lower():
        c.key('enter')
    c.wait_text(r'add boundary tests next')
