import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../sdk/python')))

import streamlit as st
import pandas as pd
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scdtestproj.settings")
django.setup()

from jobs.models import Job

st.title("SCD Platform Dashboard")

# Show all jobs
jobs = Job.objects.all().values()
df = pd.DataFrame(jobs)
st.subheader("All Jobs")
st.dataframe(df)

# Show only latest active jobs
latest_active = Job.objects.filter_latest(status="active").values()
df_latest = pd.DataFrame(latest_active)
st.subheader("Latest Active Jobs")
st.dataframe(df_latest)