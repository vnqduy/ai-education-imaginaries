"""Export the current coding into a new QualCoder 3.8.2 project (schema v14).

Source of schema: https://github.com/ccbogel/QualCoder/blob/3.8.2/src/qualcoder/__main__.py
Never overwrites a project: manual QualCoder edits must be preserved.
"""
import argparse
import collections
import csv
import datetime
import json
from pathlib import Path
import re
import sqlite3
from validate_future_coding import ROOT, WORK, rows, validate

SCHEMA = 'CREATE TABLE project (databaseversion text, date text, memo text,about text, bookmarkfile integer, bookmarkpos integer, codername text, recently_used_codes text);\nCREATE TABLE source (id integer primary key, name text, fulltext text, mediapath text, memo text, owner text, date text, av_text_id integer, risid integer, unique(name));\nCREATE TABLE code_image (imid integer primary key,id integer,x1 integer, y1 integer, width integer, height integer, cid integer, memo text, date text, owner text, important integer, pdf_page integer);\nCREATE TABLE code_av (avid integer primary key,id integer,pos0 integer, pos1 integer, cid integer, memo text, date text, owner text, important integer);\nCREATE TABLE annotation (anid integer primary key, fid integer,pos0 integer, pos1 integer, memo text, owner text, date text, unique(fid,pos0,pos1,owner));\nCREATE TABLE attribute_type (name text primary key, date text, owner text, memo text, caseOrFile text, valuetype text);\nCREATE TABLE attribute (attrid integer primary key, name text, attr_type text, value text, id integer, date text, owner text, unique(name,attr_type,id));\nCREATE TABLE case_text (id integer primary key, caseid integer, fid integer, pos0 integer, pos1 integer, owner text, date text, memo text);\nCREATE TABLE cases (caseid integer primary key, name text, memo text, owner text,date text, constraint ucm unique(name));\nCREATE TABLE code_cat (catid integer primary key, name text, owner text, date text, memo text, supercatid integer, unique(name));\nCREATE TABLE code_text (ctid integer primary key, cid integer, fid integer,seltext text, pos0 integer, pos1 integer, owner text, date text, memo text, avid integer, important integer, unique(cid,fid,pos0,pos1, owner));\nCREATE TABLE code_name (cid integer primary key, name text, memo text, catid integer, owner text,date text, color text, unique(name));\nCREATE TABLE journal (jid integer primary key, name text, jentry text, date text, owner text, unique(name));\nCREATE TABLE stored_sql (title text, description text, grouper text, ssql text, unique(title));\nCREATE TABLE graph (grid integer primary key, name text, description text, date text, scene_width integer, scene_height integer, unique(name));;\nCREATE TABLE gr_cdct_text_item (gtextid integer primary key, grid integer, x integer, y integer, supercatid integer, catid integer, cid integer, font_size integer, bold integer, isvisible integer, displaytext text);;\nCREATE TABLE gr_case_text_item (gcaseid integer primary key, grid integer, x integer, y integer, caseid integer, font_size integer, bold integer, color text, displaytext text);;\nCREATE TABLE gr_file_text_item (gfileid integer primary key, grid integer, x integer, y integer, fid integer, font_size integer, bold integer, color text, displaytext text);;\nCREATE TABLE gr_free_text_item (gfreeid integer primary key, grid integer, freetextid integer,x integer, y integer, free_text text, font_size integer, bold integer, color text,tooltip text, ctid integer,memo_ctid integer, memo_imid integer, memo_avid integer);;\nCREATE TABLE gr_cdct_line_item (glineid integer primary key, grid integer, fromcatid integer, fromcid integer, tocatid integer, tocid integer, color text, linewidth real, linetype text, isvisible integer);;\nCREATE TABLE gr_free_line_item (gflineid integer primary key, grid integer, fromfreetextid integer, fromcatid integer, fromcid integer, fromcaseid integer,fromfileid integer, fromimid integer, fromavid integer, tofreetextid integer, tocatid integer, tocid integer, tocaseid integer, tofileid integer, toimid integer, toavid integer, color text,linewidth real, linetype text);;\nCREATE TABLE gr_pix_item (grpixid integer primary key, grid integer, imid integer,x integer, y integer, px integer, py integer, w integer, h integer, filepath text,tooltip text, pdf_page integer);;\nCREATE TABLE gr_av_item (gr_avid integer primary key, grid integer, avid integer,x integer, y integer, pos0 integer, pos1 integer, filepath text, tooltip text, color text);;\nCREATE TABLE ris (risid integer, tag text, longtag text, value text);;\nCREATE TABLE manage_files_display (mfid integer primary key, name text, tblrows text, tblcolumns text, owner text);;\nCREATE TABLE files_filter (filterid integer primary key, name text, filter text, owner text);;'
OWNER = "AI-assisted import"


def export(target):
    records = rows(WORK / "coded_corpus.jsonl")
    report = validate(records, complete=True)
    if not report["valid"]:
        raise ValueError(report)
    sources = {r["ID"]: r for r in rows(ROOT / "data/source_corpus.jsonl")}
    book = json.loads((WORK / "codebook.json").read_text())
    with (ROOT / "results/article_coding.csv").open() as handle:
        metadata = {r["article_id"]: r for r in csv.DictReader(handle)}
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite an editable project: {target}")
    if target.suffix != ".qda":
        raise ValueError("Target must be a .qda directory")
    # Stage the complete database in memory before creating the deliverable.
    conn = sqlite3.connect(":memory:")
    conn.executescript(SCHEMA)
    conn.execute("CREATE TABLE coder_names (name TEXT UNIQUE NOT NULL, visibility INTEGER NOT NULL DEFAULT 1 CHECK (visibility IN (0,1)))")
    for table in ["code_text", "code_image", "code_av", "annotation"]:
        conn.execute(f"CREATE VIEW {table}_visible AS SELECT t.* FROM {table} t WHERE NOT EXISTS (SELECT 1 FROM coder_names c WHERE c.name=t.owner AND c.visibility=0)")
    conn.executemany("INSERT INTO coder_names VALUES (?,1)", [(OWNER,), ("DuyVu",)])
    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).strftime("%Y-%m-%d %H:%M:%S")
    note = "Work in progress. Imported AI-assisted coding, not independent human coding. Source text is unchanged. Categories may overlap. Article metadata and the complete original account records are retained in file memos. MISSING is absence of coding, not a highlighted segment. Repeated exact quotes without a unique locator are highlighted at every matching occurrence, marked in coding memos; review these before interpreting segment counts. Coding memos retain account and proposition links. This project is an editable copy, not automatically synchronised with the JSONL/CSV."
    conn.execute("INSERT INTO project VALUES (?,?,?,?,?,?,?,?)", ("v14",now,note,"QualCoder 3.8.2 compatible import",0,0,"DuyVu",""))
    colours = ["#88CCEE","#CC6677","#DDCC77","#117733","#332288","#AA4499","#44AA99","#999933","#882255","#661100","#6699CC","#CC99AA"]
    codes={}
    for catid,(field,entries) in enumerate(book["fields"].items(),1):
        conn.execute("INSERT INTO code_cat VALUES (?,?,?,?,?,?)",(catid,field,OWNER,now,"SIPC field: "+field,None))
        for entry in entries:
            cid=len(codes)+1; codes[field,entry["code"]]=cid
            name=field+" | "+entry["label"]
            conn.execute("INSERT INTO code_name VALUES (?,?,?,?,?,?,?)",(cid,name,json.dumps(entry,ensure_ascii=False,indent=2),catid,OWNER,now,colours[(catid-1)%len(colours)]))
    attrs=[k for k in next(iter(metadata.values())) if "__" not in k]+[f+"__missing" for f in book["fields"]]
    numeric={"year","publisher_uncertain","account_count","main_sample"}|{k for k in attrs if k.endswith("__missing")}
    for key in attrs:
        conn.execute("INSERT INTO attribute_type VALUES (?,?,?,?,?,?)",(key,now,OWNER,"Imported article metadata; blanks remain unspecified.","file","numeric" if key in numeric else "character"))
    segments=collections.defaultdict(list); ambiguous=0; evidence_count=0; occurrences=0
    for fid,record in enumerate(records,1):
        ID=record["ID"]; source=sources[ID]; text=source["full_text"]
        # Qt selections use UTF-16. Current corpus is BMP-only; fail rather than shift offsets silently.
        if any(ord(c)>65535 for c in text):
            raise ValueError(f"UTF-16 offset conversion required for {ID}")
        memo=source["title"]+"\n"+source["real_url"]+"\n\nCanonical account records (work in progress):\n"+json.dumps(record,ensure_ascii=False,indent=2)
        conn.execute("INSERT INTO source (id,name,fulltext,mediapath,memo,owner,date) VALUES (?,?,?,?,?,?,?)",(fid,ID+".txt",text,None,memo,OWNER,now))
        conn.execute("INSERT INTO cases (caseid,name,memo,owner,date) VALUES (?,?,?,?,?)",(fid,ID,source["title"],OWNER,now))
        conn.execute("INSERT INTO case_text (caseid,fid,pos0,pos1,owner,date,memo) VALUES (?,?,?,?,?,?,?)",(fid,fid,0,len(text),OWNER,now,"Article-level case; account relations are recorded in coding/file memos."))
        for key in attrs:
            conn.execute("INSERT INTO attribute (name,attr_type,value,id,date,owner) VALUES (?,?,?,?,?,?)",(key,"file",metadata[ID][key],fid,now,OWNER))
        for account in record["accounts"]:
            for field,entries in account["field_evidence"].items():
                for e in entries:
                    evidence_count+=1
                    if "quote" in e:
                        spans=[(m.start(),m.start()+len(e["quote"])) for m in re.finditer('(?='+re.escape(e["quote"])+')',text)]
                    else:
                        spans=[(e["char_start"],e["char_end"])]
                    if not spans: raise ValueError((ID,e))
                    ambiguous+=len(spans)>1
                    for start,end in spans:
                        assert 0<=start<end<=len(text)
                        occurrences+=1
                        item={"account_id":account["account_id"],"position":account["position"],"speaker":account["speaker_reference"],"future_statement":account["future_statement"],"proposition_id":e["proposition_id"],"reason":e["reason"],"original_evidence":e}
                        if len(spans)>1: item["locator_note"]=f"Repeated exact quote: {len(spans)} matching positions; original evidence does not disambiguate. All matches retained, not separate claims."
                        segments[(codes[field,e["code"]],fid,start,end,text[start:end])].append(item)
    for (cid,fid,start,end,selected),items in segments.items():
        conn.execute("INSERT INTO code_text (cid,fid,seltext,pos0,pos1,owner,date,memo) VALUES (?,?,?,?,?,?,?,?)",(cid,fid,selected,start,end,OWNER,now,json.dumps(items,ensure_ascii=False,indent=2)))
    stats={"articles":len(records),"accounts_preserved_in_memos":sum(len(r["accounts"]) for r in records),"fields":len(book["fields"]),"codes":len(codes),"evidence_entries":evidence_count,"repeated_quote_entries":ambiguous,"evidence_occurrences":occurrences,"coded_segments":len(segments)}
    conn.execute("INSERT INTO journal (name,jentry,date,owner) VALUES (?,?,?,?)",("Import notes",note+"\n\n"+json.dumps(stats,indent=2),now,OWNER))
    assert conn.execute("PRAGMA integrity_check").fetchone()[0]=="ok"
    assert conn.execute("SELECT count(*) FROM code_text c JOIN source s ON c.fid=s.id WHERE c.seltext != substr(s.fulltext,c.pos0+1,c.pos1-c.pos0)").fetchone()[0]==0
    assert sum(len(json.loads(m)) for (m,) in conn.execute("SELECT memo FROM code_text"))==occurrences
    # Independently verify imported article-level presence against every CSV code cell.
    for fid,record in enumerate(records,1):
        actual={r[0] for r in conn.execute("SELECT DISTINCT cid FROM code_text WHERE fid=?",(fid,))}
        expected={cid for (f,c),cid in codes.items() if metadata[record["ID"]][f+"__"+c]=="1"}
        assert actual==expected,record["ID"]
    conn.commit()
    target.mkdir(parents=True)
    for sub in ["documents","images","audio","video"]: (target/sub).mkdir()
    disk=sqlite3.connect(target/"data.qda");conn.backup(disk)
    assert disk.execute("PRAGMA integrity_check").fetchone()[0]=="ok"
    disk.close();conn.close()
    print(json.dumps({"project":str(target),**stats,"validation":"SQLite integrity, exact source spans and full CSV presence agreement passed"},ensure_ascii=False,indent=2))

if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target",nargs="?",type=Path,default=ROOT/"results/ai_news_edu.qda")
    export(parser.parse_args().target)
