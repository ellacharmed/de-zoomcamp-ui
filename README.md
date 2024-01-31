<div align="center">
  <div id="user-content-toc">
    <ul>
      <summary><h1 style="display: inline-block;">👨‍🔧 Data Engineering Zoocamp UI 🎨</h1></summary>
    </ul>
  </div>

  <p>An Interactive UI for the DE Zoomcamp Course provided by DataTalksClub</p>
    <a href="https://dezoomcamp.streamlit.app/" target="_blank">Demo</a>
    🌌
    <a href="https://github.com/Hamagistral/de-zoomcamp-ui/issues" target="_blank">Request Feature</a>
</div>
<br>
<div align="center">
      <a href="https://dezoomcamp.streamlit.app/"><img src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg"/></a>
      <img src="https://img.shields.io/github/stars/hamagistral/de-zoomcamp-ui?color=blue&style=social"/>
</div>

<hr>

![home](https://github.com/Hamagistral/de-zoomcamp-ui/assets/66017329/c24799d2-5c4b-4f14-9d85-78d09ab975ee)


## 🎯 Motivation

The DE Zoomcamp UI project was born out of the need for a more accessible and organized learning experience for the **DE Zoomcamp Course by DataTalksClub**. As a student eager to dive into data engineering and learn modern technologies like Google Cloud, Docker, Terraform, Prefect, Spark, Kafka and more, I found it tiring to navigate through the course materials on GitHub and YouTube. Inspired by the clean and intuitive UI of CS50, I decided to create a simplified interface that brings together all the course resources in one place. This streamlit app aims to provide a user-friendly and streamlined experience, making it easier for learners like me to explore the course, answer homework questions directly in the app, and gain hands-on experience with data engineering technologies. By sharing this project, I hope to help others on their journey to becoming skilled data engineers.

## 🚀 Features

- **Easy navigation:** Access course materials, READMEs, YouTube videos, and homework assignments with a simple and intuitive interface.
- **Interactive learning:** Experiment with code examples, answer homework questions, and check their answers directly from the web app.
- **Clean and inspired design:** UI inspiration from the popular CS50 course, the UI provides a clean and enjoyable learning experience.

## 🚨 Disclaimer

This UI is created by a student as a personal project to facilitate personal learning and is not officially affiliated with DataTalksClub or the DE Zoomcamp course. All course materials and resources belong to their respective owners.

## 👨‍🏫 Acknowledgements

Special thanks to DataTalksClub for providing the DE Zoomcamp course and inspiring this UI project.

## 🛠️ Technologies Used

This simple UI was built using Streamlit.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
<img src="https://user-images.githubusercontent.com/66017329/223900076-e1d5c1e5-7c4d-4b73-84e7-ae7d66149bc6.png" alt="streamlit" width="120">

## 💻 Usage

1. Clone the repository:

```
git clone https://github.com/hamagistral/de-zoomcamp-ui.git
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

3. Run the app:

First run, install venv first; subsequent runs be sure to activate `mba zoomcampui`.

```bash
streamlit run dezoomcamp/DE_Zoomcamp.py
```

4. Access the app in your browser at http://localhost:8501

## Blueprint for restructure plans

As it is unfair of current cohort to expect Hamza to keep updating this in perpetuity, I'm taking the opportunity of updating with 2024 content for `data-engineering-zoomcamp` and also changing the structure of the pages.

- [ ] Sidebar: Use Radio buttons for 3 courses and cohorts
- [ ] Sidebar: Unselected course/cohort should remain hidden
- this would ensure Sidebar does not get too long, and only the course in context is being shown. I don't need to see content list of courses not currently selected.
- [ ] Main Page: Add mine to Hamza's contributor & copyright as a footer for every page. 
- Easier to edit? Instead of at every page
- Ideas: `st.container` but seems that `st.footer` has been deprecated
- [ ] Main Page: ultimately, content needs to be scraped and "plugged-in". Not going to re-edit for perpetuity if repos are edited at any time.

- This however won't help for cases when the content is in its own repo - examples for some like Prefect and Mage lessons.
- [ ] Edit main script entrypoint name if catering to all courses, as just `zoomcamp.py`


## 📨 Contact Me

[LinkedIn](https://www.linkedin.com/in/hamza-elbelghiti/) •
[Website](https://hamagistral.me) •
[Gmail](hamza.lbelghiti@gmail.com)
