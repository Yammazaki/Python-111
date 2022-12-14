from hh import get_max_page,get_hh_jobs
from save import save_to_csv
from db import data_base
from flask import Flask, render_template, request, redirect, send_file


app = Flask('site_project')

db = {}

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/report')
def report():
  keyword = (request.args.get('keyword'))
  if keyword is not None:
    keyword = keyword.lower()
    getDb = db.get(keyword)
    if getDb:
      jobs = getDb
    else:
      jobs = get_hh_jobs(keyword)
      db[keyword] = jobs
    print(jobs)
  else:
    return redirect('/')
  return render_template('report.html', searchBy = keyword, results_number = len(jobs), jobs = jobs)

@app.route('/export')
def export():
  try:
    keyword = (request.args.get('keyword'))
    if not keyword:
      raise Exception()
    keyword = keyword.lower()
    jobs = db.get(keyword)
    if not jobs:
      raise Exception()
    save_to_csv(jobs)
    return send_file('vacancy.csv')
  except:
    return redirect('/')
    
app.run(host='0.0.0.0')


def parsing(): 
    max_page = get_max_page() 
    jobs = get_hh_jobs(max_page)
    save_to_csv(jobs)
    data_base(jobs)

