"""Capture Crush's native themed workspace without starting an agent turn."""
import json


def prepare(c):
    c.git_fixture()
    c.copy(f'themes/{c.slug}.json', f'.config/crush/themes/{c.slug}.json')
    config = {'options': {'tui': {'active_theme': c.slug}, 'disable_provider_auto_update': True,
                          'disable_metrics': True, 'disable_default_providers': True},
              'providers': {'capture': {'name': 'Offline screenshot fixture', 'type': 'openai-compat',
                  'base_url': 'http://127.0.0.1:9/v1', 'api_key': 'capture-not-a-real-key',
                  'models': [{'id': 'fixture', 'name': 'Offline fixture', 'context_window': 128000, 'default_max_tokens': 4096}]}},
              'models': {'large': {'model': 'fixture', 'provider': 'capture'},
                         'small': {'model': 'fixture', 'provider': 'capture'}}}
    c.write('.config/crush/crush.json', json.dumps(config))
    c.env['CRUSH_GLOBAL_CONFIG'] = str(c.home / '.config/crush')
    return ['crush']


def drive(c):
    c.wait_text(r'ctrl\+p|New Session|New Chat|Welcome to Crush|trust this')
    if 'trust' in c.text().lower():
        c.key('enter')
    c.type('Review src/FieldRenderer.ts')  # Do not submit; capture the actual input UI.
