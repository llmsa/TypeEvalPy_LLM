import json
import os

from scalpel.typeinfer.typeinfer import TypeInference


def list_python_files(folder_path):
    python_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
    return python_files


folder_path = "../micro-benchmark/analysis_sensitivities/object_sensitivity"

python_files = list_python_files(folder_path)

for file in python_files:
    print(file)
    try:
        json_file_path = file.replace(".py", "_gt.json")

        if os.path.exists(json_file_path):
            print(f"JSON file already exists: {json_file_path}")
            continue

        inferer = TypeInference(name=file, entry_point=file)
        inferer.infer_types()
        inferred = inferer.get_types()
        print(inferred)

        with open(json_file_path, "w") as json_file:
            # json.dump(inferred, json_file)
            inferred_serializable = [
                {k: list(v) if isinstance(v, set) else v for k, v in d.items()}
                for d in inferred
            ]
            inferred_serializable.sort(key=lambda x: x["line_number"])
            json.dump(inferred_serializable, json_file, indent=4)
    except Exception as e:
        print(e)
