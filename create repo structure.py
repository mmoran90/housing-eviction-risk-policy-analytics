from pathlib import Path

folders = [
    "data/raw/acs",
    "data/raw/hud_chas",
    "data/raw/eviction_lab",
    "data/raw/crosswalks",
    "data/interim",
    "data/processed",
    "data/external",
    "notebooks",
    "src/data",
    "src/features",
    "src/modeling",
    "src/policy",
    "src/visualization",
    "app/pages",
    "app/assets",
    "reports/figures",
    "reports/tables",
    "models/baseline",
    "models/boosted",
    "models/artifacts",
    "tests",
]

files = [
    "README.md",
    "requirements.txt",
    ".gitignore",
    ".env.example",
    "src/__init__.py",
    "src/config.py",
    "src/utils.py",
    "src/data/__init__.py",
    "src/features/__init__.py",
    "src/modeling/__init__.py",
    "src/policy/__init__.py",
    "src/visualization/__init__.py",
    "app/Home.py",
    "tests/test_build_panel.py",
    "tests/test_target_definition.py",
    "tests/test_feature_engineering.py",
]

for folder in folders:
    Path(folder).mkdir(parents=True, exist_ok=True)

for file in files:
    Path(file).touch(exist_ok=True)

print("Project scaffold created.")