"""Assemble report/report.html from report/template.html + the three data files.
Run from the repo root after prep_report.py, prep_round2.py, prep_round3.py:
    python report/build_report.py
"""
data = open("report_data.json").read()
r2 = open("round2.json").read()
r3 = open("round3_report.json").read()
tpl = open("report/template.html", encoding="utf-8").read()
out = tpl.replace("/*__DATA__*/", data).replace("/*__DATA2__*/", r2).replace("/*__DATA3__*/", r3)
open("report/report.html", "w", encoding="utf-8").write(out)
print("report/report.html written,", len(out) // 1024, "KB")
