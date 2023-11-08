import requests

def create_(path, token):
    url = 'https://cloud-api.yandex.net/v1/disk/resources'

    headers = {
        'Authorization': f'OAuth {str(token)}'
    }

    result = requests.put(f'{url}?path={path}', headers=headers)
    return result.status_code

if __name__ == '__main__':
    token = 'y0_AgAAAAAJQB6iAADLWwAAAADokSx_ngpuJ4O8Q5iJLkAetch0yV35qLw'
    create_('Hello', token)