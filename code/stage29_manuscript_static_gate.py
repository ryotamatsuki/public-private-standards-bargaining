"""Stage29 pre-submission manuscript static gate.

This gate is NOT a substitute for LaTeX compile, mathematical
independent review, or bibliographic source verification.
It verifies modular section completeness, precise theorem-scope
guards, complete crossref/citation keys, and prohibition of
literature-firstness overclaims. All references resolve in source.
"""
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
ROOT_TEX=ROOT/"manuscript/main.tex"
BIB=ROOT/"manuscript/references.bib"
FILES=[
"sections/02_model.tex",
"sections/03_policy.tex",
"sections/04_equilibrium.tex",
"sections/05_welfare.tex",
"sections/06_robustness.tex",
"sections/01_introduction.tex",
"sections/07_conclusion.tex",
"appendix/A_proofs.tex",
"appendix/B_certificates.tex",
]

def main():
    main=ROOT_TEX.read_text()
    assert "\\bibliography{references}" in main
    assert "\\appendix" in main
    texts={x:(ROOT/"manuscript"/x).read_text() for x in FILES}
    full=main+"\n"+"\n".join(texts.values())
    for item in FILES:
        assert "\\input{"+item.removesuffix(".tex")+"}" in main,item
        assert len(texts[item].split())>120,(item,len(texts[item].split()))
    for required in ("pure-strategy","mixed","prior",
                     "sunk","retrofit","consumer surplus",
                     "at least two","three-country","Costinot",
                     "Gandal", "Ruiz"):
        assert required.lower() in full.lower(),required
    assert not re.search(r"\bStage\s*\d+\b",full), "Internal research-stage labels found in journal-facing manuscript"
    banned=["first to endogenize","first to use a voting",
            "the unique SPE","our theory holds in every economy",
            "majority is always efficient"]
    for bad in banned:
        assert bad.lower() not in full.lower(),bad
    labels=re.findall(r"\\label\{([^}]+)\}",full)
    refs=re.findall(r"\\(?:eqref|ref)\{([^}]+)\}",full)
    assert len(set(labels))==len(labels),[i for i in labels if labels.count(i)>1]
    missing=set(refs)-set(labels)
    assert not missing,missing
    bib=BIB.read_text()
    bibkeys=set(re.findall(r"@\w+\s*\{\s*([^,\s]+)",bib))
    cites=[]
    for found in re.finditer(r"\\cite(?:t|p|alp|alt|author|year)?(?:\[[^]]*\])?\{([^}]+)\}",full):
        cites.extend([x.strip() for x in found.group(1).split(",")])
    missing_bib=set(cites)-bibkeys
    assert not missing_bib,missing_bib
    print("PASS ST29 independent manuscript file inventory:",len(FILES))
    print("PASS labels",len(labels),"references",len(refs),
          "bibitems",len(bibkeys),"citations",len(cites))
    print("PASS claim quantifiers, no broad priority overclaims")
    for section,content in texts.items():
        print("SECTION",section,len(content.split()),"space-delimited words")

if __name__=="__main__":
    main()
