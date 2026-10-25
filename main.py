import argparse,shutil
from pathlib import Path

def plan_moves(folder):
    base=Path(folder).resolve()
    if not base.is_dir(): raise NotADirectoryError(base)
    plan=[]
    for p in sorted(base.iterdir()):
        if not p.is_file(): continue
        ext=p.suffix.lower().lstrip(".") or "no-extension"
        dest=base/ext/p.name
        if p.parent.name==ext: continue
        plan.append((p,dest))
    return plan

def apply_moves(plan):
    moved=[]
    for src,dest in plan:
        dest.parent.mkdir(parents=True,exist_ok=True)
        candidate=dest; i=1
        while candidate.exists(): candidate=dest.with_name(f"{dest.stem}_{i}{dest.suffix}"); i+=1
        shutil.move(str(src),str(candidate)); moved.append((src,candidate))
    return moved

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("folder"); ap.add_argument("--apply",action="store_true",help="actually move files (default is dry-run)"); a=ap.parse_args(); plan=plan_moves(a.folder)
    for s,d in plan: print(f"{s.name} -> {d.relative_to(Path(a.folder).resolve())}")
    if a.apply: apply_moves(plan); print(f"Moved {len(plan)} files")
    else: print(f"Dry run: {len(plan)} planned moves. Add --apply to execute.")
if __name__=="__main__": main()
