from argparse import ArgumentParser
from requests import Session


def add_nodes():
    print('Adding some nodes to the repository')
    nodes = [
        {'type': 'Source', 'name': 'CSV Reader', 'description': 'read from input file'},
        {'type': 'Manipulator', 'name': 'Row Sampling', 'description': 'randomly sample data', 'predecessor': 1},
        {'type': 'Manipulator', 'name': 'Column Filter', 'description': 'only first 3 columns', 'predecessor': 2},
        {'type': 'Visualizer', 'name': 'Scatter Plot', 'description': 'show x ~ y scatter plot', 'predecessor': 3},
        {'type': 'Visualizer', 'name': 'Table View', 'description': 'select some rows', 'predecessor': 3},
        {'type': 'Manipulator', 'name': 'Row Filter', 'description': 'filter rows to keep', 'predecessor': 5},
        {'type': 'Sink', 'name': 'CSV Writer', 'description': 'write to output file', 'predecessor': 6}
    ]
    session = Session()
    url = f'{base_url}/nodes'
    for node in nodes:
        print(f'POST <{node}> to <{url}>')
        response = session.post(url=url, json=node)
        node = response.json()
        print(f'Added node <{node}>')


def get_all_nodes():
    session = Session()
    url = f'{base_url}/nodes'
    print(f'GET <{url}>')
    response = session.get(url=url)
    nodes = response.json()
    for node in nodes:
        print(node)


def main():
    if action == 'add_nodes':
        add_nodes()
    elif action == 'get_all_nodes':
        get_all_nodes()
    else:
        raise ValueError(f'Sorry, cannot perform <{action}> action')


if __name__ == '__main__':
    parser = ArgumentParser(description='Make calls to the Nodes REST API')
    parser.add_argument('action', help='Action to perform (\'add_nodes\' / \'get_all_nodes\' / ...)', type=str)
    parser.add_argument('--base_url', help='The base url of this API', type=str, default='http://localhost:8081/api')
    args = parser.parse_args()
    action = args.action
    base_url = args.base_url
    main()
