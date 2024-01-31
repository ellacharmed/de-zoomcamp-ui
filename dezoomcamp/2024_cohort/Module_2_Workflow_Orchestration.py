import streamlit as st
from st_pages import add_page_title

add_page_title(layout="wide")

st.success("""
> If you're looking for Airflow videos from the 2022 edition, check the [2022 cohort folder](../cohorts/2022/week_2_data_ingestion/).  
> If you're looking for Prefect videos from the 2023 edition, check the [2023 cohort folder](../cohorts/2023/week_2_data_ingestion/).
""")

st.markdown("---")

st.markdown("""* ⭐ If you are enjoying your learning experience please leave a Star for the original Author <iframe src="https://ghbtns.com/github-btn.html?user=hamagistral&repo=de-zoomcamp-ui&type=star&count=true"  width="150" height="20" title="hamagistral GitHub"></iframe>
""", unsafe_allow_html=True)

st.markdown("""* ⭐ If you like my version please leave a Star to encourage me to keep going <iframe src="https://ghbtns.com/github-btn.html?user=ellacharmed&repo=de-zoomcamp-ui&type=star&count=true"  width="150" height="20" title="ellacharmed GitHub"></iframe>
""", unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
Welcome to Week 2 of the Data Engineering Zoomcamp! 🚀😤 This week, we'll be covering workflow orchestration with Mage.

Mage is an open-source, hybrid framework for transforming and integrating data. ✨

This week, you'll learn how to use the Mage platform to author and share _magical_ data pipelines. This will all be covered in the course, but if you'd like to learn a bit more about Mage, check out our docs [here](https://docs.mage.ai/introduction/overview).""")

st.markdown("---")

st.markdown("## 1. 📯 Intro to Orchestration")

st.markdown("In this section, we'll cover the basics of workflow orchestration. We'll discuss what it is, why it's important, and how it can be used to build data pipelines.")

st.video("https://www.youtube.com/watch?v=Li8-MWHhTbo&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb")


st.markdown("### Resources")

st.info("- [Slides](https://docs.google.com/presentation/d/17zSxG5Z-tidmgY-9l7Al1cPmz4Slh4VPK6o2sryFYvw/)")

st.markdown("---")

st.markdown("## 2. 🧙‍♂️ Intro to Mage")

st.markdown("In this section, we'll introduce the Mage platform. We'll cover what makes Mage different from other orchestrators, the fundamental concepts behind Mage, and how to get started. To cap it off, we'll spin Mage up via Docker 🐳 and run a simple pipeline.")

st.markdown("### 2.1. What is Mage?")
st.video("https://www.youtube.com/watch?v=AicKRcK3pa4&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb")

st.markdown("### 2.2. Configuring Mage")
st.video("https://www.youtube.com/watch?v=tNiV7Wp08XE&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb")

st.markdown("### 2.3. A Simple Pipeline")
st.video("https://www.youtube.com/watch?v=stI-gg4QBnI&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb")

st.markdown("#### Resources")
st.info("""
- [Getting Started Repo](https://github.com/mage-ai/mage-zoomcamp)
- [Slides](https://docs.google.com/presentation/d/1y_5p3sxr6Xh1RqE6N8o2280gUzAdiic2hPhYUUD6l88/)
""")

st.markdown("---")

st.markdown("## 3. 🐘 ETL: API to Postgres")

st.markdown("Hooray! Mage is up and running. Now, let's build a _real_ pipeline. In this section, we'll build a simple ETL pipeline that loads data from an API into a Postgres database. Our database will be built using Docker— it will be running locally, but it's the same as if it were running in the cloud.")

st.markdown("### 3.1. Configuring Postgres")
st.video("https://www.youtube.com/watch?v=pmhI-ezd3BE&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb")

st.markdown("### 3.2. Writing an ETL Pipeline")
st.video("https://www.youtube.com/watch?v=Maidfe7oKLs&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb")

st.markdown("### Resources")

st.info("""
- [Taxi Dataset](https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz)
- [Sample loading block](https://github.com/mage-ai/mage-zoomcamp/blob/solutions/magic-zoomcamp/data_loaders/load_nyc_taxi_data.py)
""")

st.markdown("---")

st.markdown("## 4. 🤓 ETL: API to GCS")

st.markdown("""
Ok, so we've written data _locally_ to a database, but what about the cloud? In this tutorial, we'll walk through the process of using Mage to extract, transform, and load data from an API to Google Cloud Storage (GCS). 

We'll cover both writing _partitioned_ and _unpartitioned_ data to GCS and discuss _why_ you might want to do one over the other. Many data teams start with extracting data from a source and writing it to a data lake _before_ loading it to a structured data source, like a database.
""")

st.markdown("### 4.1. Configuring GCP")
st.video("https://www.youtube.com/watch?v=00LP360iYvE&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb")

st.markdown("### 4.2. Writing an ETL Pipeline")
st.video("https://www.youtube.com/watch?v=w0XmcASRUnc&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb")

st.markdown("### Resources")

st.info("- [DTC Zoomcamp GCP repo](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/week_1_basics_n_setup/1_terraform_gcp/2_gcp_overview.md)")


st.markdown("1.4.1 - Setting up the Environment on Google Cloud")
st.video("https://youtu.be/ae-CV2KfoN0?si=OrZXLL4KtHvjsJFK")

st.markdown("---")

st.markdown("## 5. 🔍 ETL: GCS to BigQuery")

st.markdown("Now that we've written data to GCS, let's load it into BigQuery. In this section, we'll walk through the process of using Mage to load our data from GCS to BigQuery. This closely mirrors a very common data engineering workflow: loading data from a data lake into a data warehouse.")

st.markdown("### 5.1. Writing an ETL Pipeline")
st.video("https://www.youtube.com/watch?v=JKp_uzM-XsM")

st.markdown("---")

st.markdown("## 6. 👨‍💻 Parameterized Execution")

st.markdown("By now you're familiar with building pipelines, but what about adding parameters? In this video, we'll discuss some built-in runtime variables that exist in Mage and show you how to define your own! We'll also cover how to use these variables to parameterize your pipelines. Finally, we'll talk about what it means to *backfill* a pipeline and how to do it in Mage.")

st.markdown("### 6.1. Parameterized Execution")
st.video("https://www.youtube.com/watch?v=H0hWjWxB-rg&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb")

st.markdown("### 6.2. Backfills")
st.video("https://www.youtube.com/watch?v=ZoeC6Ag5gQc&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb")

st.markdown("#### Resources")

st.info("""
- [Mage Variables Overview](https://docs.mage.ai/development/variables/overview)  
- [Mage Runtime Variables](https://docs.mage.ai/getting-started/runtime-variable)
""")

st.markdown("---")

st.markdown("## 7. 🤖 Deployment (Optional)")

st.markdown("In this section, we'll cover deploying Mage using Terraform and Google Cloud. This section is optional— it's not *necessary* to learn Mage, but it might be helpful if you're interested in creating a fully deployed project. If you're using Mage in your final project, you'll need to deploy it to the cloud.")

st.markdown("### 7.1. Deployment Prerequisites")
st.video("https://www.youtube.com/watch?v=zAwAX5sxqsg&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb")

st.markdown("### 7.2. Google Cloud Permissions")
st.video("https://www.youtube.com/watch?v=O_H7DCmq2rA&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb")

st.markdown("### 7.3. Deploying to Google Cloud - Part 1")
st.video("https://www.youtube.com/watch?v=9A872B5hb_0&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb")

st.markdown("### 7.4. Deploying to Google Cloud - Part 2")
st.video("https://www.youtube.com/watch?v=0YExsb2HgLI&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb")

st.markdown("#### Resources")

st.info("""
- [Installing Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)  
- [Installing `gcloud` CLI](https://cloud.google.com/sdk/docs/install)  
- [Mage Terraform Templates](https://github.com/mage-ai/mage-ai-terraform-templates)
- [Terraform](https://docs.mage.ai/production/deploying-to-cloud/using-terraform)
- [Deploying to GCP with Terraform](https://docs.mage.ai/production/deploying-to-cloud/gcp/setup)
""")

st.markdown("---")

st.markdown("## 8. 📝 Practicals")

st.markdown("### 8.1. Lessons")


st.markdown("""
## Data Engineering Zoomcamp - Week 2

Welcome to DE Zoomcamp with Mage! 

Mage is an open-source, hybrid framework for transforming and integrating data. ✨

In this module, you'll learn how to use the Mage platform to author and share _magical_ data pipelines. This will all be covered in the course, but if you'd like to learn a bit more about Mage, check out our docs [here](https://docs.mage.ai/introduction/overview). 
""")

st.markdown("#### Resources")
st.info("""
- [Get Started](https://github.com/mage-ai/mage-zoomcamp?tab=readme-ov-file#lets-get-started)
- [Assistance](https://github.com/mage-ai/mage-zoomcamp?tab=readme-ov-file#assistance)
""")


st.markdown("""
## Let's get started

This repo contains a Docker Compose template for getting started with a new Mage project. It requires Docker to be installed locally. If Docker is not installed, please follow the instructions [here](https://docs.docker.com/get-docker/). 

You can start by cloning the repo:

```bash
git clone https://github.com/mage-ai/mage-zoomcamp.git mage-zoomcamp
```

Navigate to the repo:

```bash
cd mage-data-engineering-zoomcamp
```

Rename `dev.env` to simply `.env`— this will _ensure_ the file is not committed to Git by accident, since it _will_ contain credentials in the future.

Now, let's build the container

```bash
docker compose build
```

Finally, start the Docker container:

```bash
docker compose up
```

Now, navigate to http://localhost:6789 in your browser! Voila! You're ready to get started with the course. 
""")

st.markdown("""
### What just happened?

We just initialized a new mage repository. It will be present in your project under the name `magic-zoomcamp`. If you changed the varable `PROJECT_NAME` in the `.env` file, it will be named whatever you set it to.

If mage has a new update, pull the latest image with docker and then build the `yaml` again.

```bash
docker pull mageai/mageai:latest
docker compose build
```

This repository should have the following structure:

```
.
├── mage_data
│   └── magic-zoomcamp
├── magic-zoomcamp
│   ├── __pycache__
│   ├── charts
│   ├── custom
│   ├── data_exporters
│   ├── data_loaders
│   ├── dbt
│   ├── extensions
│   ├── interactions
│   ├── pipelines
│   ├── scratchpads
│   ├── transformers
│   ├── utils
│   ├── __init__.py
│   ├── io_config.yaml
│   ├── metadata.yaml
│   └── requirements.txt
├── Dockerfile
├── README.md
├── dev.env
├── docker-compose.yml
└── requirements.txt
""")

st.markdown("#### Assistance")
st.info("""
1. [Mage Docs](https://docs.mage.ai/introduction/overview): a good place to understand Mage functionality or concepts.
1. [Mage Slack](https://www.mage.ai/chat): a good place to ask questions or get help from the Mage team.
1. [DTC Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/week_2_workflow_orchestration): a good place to get help from the community on course-specific inquireies.
1. [Mage GitHub](https://github.com/mage-ai/mage-ai): a good place to open issues or feature requests.
""")

st.markdown("### 8.2. Homework")

st.markdown("""We've prepared a short exercise to test you on what you've learned this week. You can find the homework [here](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2024/02-workflow-orchestration/homework.md). This follows closely from the contents of the course and shouldn't take more than an hour or two to complete. 😄""")

st.markdown("## 9.👣 Next Steps")

st.markdown("Congratulations! You've completed Week 2 of the Data Engineering Zoomcamp. We hope you've enjoyed learning about Mage and that you're excited to use it in your final project. If you have any questions, feel free to reach out to us on Slack. Be sure to check out our 'Next Steps' video for some inspiration for the rest of your journey 😄.")

st.video("https://www.youtube.com/watch?v=uUtj7N0TleQ")

st.info("""
**Resources**:
- [Slides](https://docs.google.com/presentation/d/1yN-e22VNwezmPfKrZkgXQVrX5owDb285I2HxHWgmAEQ/edit#slide=id.g262fb0d2905_0_12)

**Additional Resources**:

- [Mage Docs](https://docs.mage.ai/)
- [Mage Guides](https://docs.mage.ai/guides)
- [Mage Slack](https://www.mage.ai/chat)""")

st.markdown("---")

st.caption("""
🖼️ Course UI was made by [Hamagistral](https://github.com/Hamagistral) and this version updated by [ellacharmed](https://github.com/ellacharmed)
""")

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True) 