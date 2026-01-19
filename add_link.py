import argparse
from pathlib import Path
from urllib.parse import quote

REPO_URL = "https://github.com/APS106/APS106-winter-2026-tutorials"
REDIRECT_URL = "https://jupyter.utoronto.ca/hub/user-redirect/git-pull"
BRANCH = "master"
ROOT = Path(__file__).parent


def build_link(tutorial_name: str, sub_folder: str, filename: str) -> str:
    """
    Build a JupyterHub git-pull link for the requested file.
    """
    repo_q = quote(REPO_URL, safe="")
    path_q = quote(f"APS106-winter-2026-tutorials/{tutorial_name}/{sub_folder}/{filename}")
    return f"{REDIRECT_URL}?repo={repo_q}&urlpath=tree%2F{path_q}&branch={BRANCH}"


def collect_links_for_tutorial(tutorial_path: Path) -> dict[str, tuple[str | None, str | None]]:
    """
    Collect starter and complete links for every sub-folder inside a tutorial.
    Returns a mapping of "tutorial/subfolder" -> (starter_link, complete_link).
    """
    links: dict[str, tuple[str | None, str | None]] = {}
    tutorial_name = tutorial_path.name

    for sub_folder in sorted(p for p in tutorial_path.iterdir() if p.is_dir()):
        starter_link: str | None = None
        complete_link: str | None = None

        for nb in sorted(sub_folder.glob("*.ipynb")):
            link = build_link(tutorial_name, sub_folder.name, nb.name)
            name_lower = nb.name.lower()

            if "starter" in name_lower:
                starter_link = link
            elif "complete" in name_lower:
                complete_link = link

        # Only record sub-folders that actually contain notebooks
        if starter_link or complete_link:
            key = f"{tutorial_name}/{sub_folder.name}"
            links[key] = (starter_link, complete_link)

    return links


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tutorial_name", type=str, default=None)
    args = parser.parse_args()

    target_dirs = []
    if args.tutorial_name:
        target = ROOT / args.tutorial_name
        if target.is_dir():
            target_dirs.append(target)
    else:
        target_dirs = [p for p in ROOT.iterdir() if p.is_dir() and p.name.startswith("tutorial")]

    links: dict[str, tuple[str | None, str | None]] = {}
    for tutorial_path in target_dirs:
        links.update(collect_links_for_tutorial(tutorial_path))

    with open(ROOT / "links.txt", "w") as f:
        for key in sorted(links):
            starter_link, complete_link = links[key]
            f.write(f"{key}\n{starter_link or ''}\n{complete_link or ''}\n\n")


if __name__ == "__main__":
    main()