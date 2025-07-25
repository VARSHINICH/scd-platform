import yaml
import sys
import os

def load_spec():
    with open(os.path.join(os.path.dirname(__file__), '../scdql/scd_models.yaml')) as f:
        return yaml.safe_load(f)

def list_models():
    spec = load_spec()
    print("SCD Models:")
    for model in spec.get('models', []):
        print(f" - {model['name']}")

def list_queries():
    spec = load_spec()
    print("SCD Queries:")
    for query in spec.get('queries', []):
        print(f" - {query['name']} (model: {query['model']})")

def show_query(query_name):
    spec = load_spec()
    for query in spec.get('queries', []):
        if query['name'] == query_name:
            print(f"Query: {query['name']}")
            print(f"Model: {query['model']}")
            print("Filters:")
            for k, v in query.get('filters', {}).items():
                print(f"  {k}: {v}")
            return
    print("Query not found.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: scdcli.py [list-models|list-queries|show-query <query_name>]")
        sys.exit(1)
    if sys.argv[1] == "list-models":
        list_models()
    elif sys.argv[1] == "list-queries":
        list_queries()
    elif sys.argv[1] == "show-query" and len(sys.argv) == 3:
        show_query(sys.argv[2])
    else:
        print("Invalid command.")