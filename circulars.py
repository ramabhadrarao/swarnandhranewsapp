import mysql.connector
import streamlit as st
import pandas as pd 
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
import numpy as np

logo = Image.open(r'swrnlogo.png')
#import cv2
#import plotly.express as px
import io
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
bootstrap="<link href='https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3' crossorigin='anonymous'>"
st.markdown(bootstrap,unsafe_allow_html=True)
mydb = mysql.connector.connect(**st.secrets["mysql"])
mycursor = mydb.cursor()
with st.sidebar:
    choose = option_menu("Swarnandhra Exam Branch Info", ["About", "Circulars", "Notifications",  "Contact"],
                         icons=['house', 'bell', 'bell-fill', 'person lines fill'],
                         menu_icon="award", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )





if choose == "About":
  st.header("About")
  col1, col2 = st.columns( [0.2, 0.8])
  with col1:
      st.image(logo)
  with col2:
    txt = '''
        <div class='card' style='width: 100%;'>
        
        <div class='card-body'>
        <h5 class='card-title'>Profile</h5>
        <p class='card-text' style='text-align:justify'> Swarnandhra College of Engineering and Technology (Eamcet Code: SWRN ) was established in the year 2001 at Seetharampuram, Narsapur, West Godavari District, Andhra Pradesh by The Vasista Educational Society with a vision to empower the students to become technologically sound, innovative and emotionally matured to face the challenges of the globalized world economy. All the courses are approved by All India Council of Technical Education (AICTE), New Delhi (Statutory body of Government of India) and Department of Technical Education (DTE), Hyderabad, Government of AndhraPradesh.</p>
        <p class='card-text' style='text-align:justify'>SCET offers UG B.Tech. programmes in Civil Engineering, Mechanical Engineering, Electrical and Electronics Engineering, Computer Science and Engineering, Electronics and Communication Engineering and Information Technology and PG M.Tech programmes in CAD/CAM, Power Electronics, VLSISD, Computer Science & Engineering, Nanotechnology, and Structural Engineering along with Master of Business Administration and Master of Computer Applications.</p>
        <p class='card-text' style='text-align:justify'>The campus is located at seetharampuram on NH-214A, 5KM from Narsapur Town. This college has fully developed infrastructural facilities with a built up area of 38,243 Sq mts consisting of 60 modern spacious class rooms,14 Tutorial Rooms, 04 Seminar Halls, 04 Drawing Halls, 15 Computer Labs,33 Laboratories, 3 Workshops, 5 Girls Common Rooms, Canteen, Conference Hall, Central Library along with Digital Library.All departments are functional with qualified teaching faculty as per AICTE norms.</p>
        <p class='card-text' style='text-align:justify'>The institution is always ahead in the pursuit of excellence. The Management of the institution believes in adopting the changes from time to time by introducing the latest advanced technologies in the curriculum by providing all necessary infrastructural and instructional facilities. The institution adopted Outcome Based Education (OBE) and Choice Based Credit System (CBCS) for academic enhancement. It has well qualified and experienced faculty involved in innovative, quality pedagogy and R & D activities. Projects worth of 1,05,41,000/-were sponsored to the Institution by IACQER, DST, UGC, DAE, DRDO, and AICTE. Presently, the institution has three research projects worth Rs. 25 lakhs sponsored by DST, DRDO, and UGC. The institution has three recognized research centers, among which the Mechanical Engineering department is recognized by JNTUK, Kakinada. The campus is located at seetharampuram on NH-214A, 5KM from Narsapur Town. This college has fully developed infrastructural facilities with a built up area of 38,243 Sq mts consisting of 60 modern spacious class rooms,14 Tutorial Rooms, 04 Seminar Halls, 04 Drawing Halls, 15 Computer Labs,33 Laboratories, 3 Workshops, 5 Girls Common Rooms, Canteen, Conference Hall, Central Library along with Digital Library.All departments are functional with qualified teaching faculty as per AICTE norms.
        The Institute imparts training to Under Graduate engineering courses</p>
        </div>
        </div>
        '''
    st.markdown(txt,unsafe_allow_html=True)
    

if choose == "Circulars":
      st.header("Circulars:")
      mycursor.execute("select tblposts.id as pid,tblposts.PostTitle as posttitle,tblposts.PostImage,tblcategory.CategoryName as category,tblcategory.id as cid,tblsubcategory.Subcategory as subcategory,tblposts.PostDetails as postdetails,tblposts.PostingDate as postingdate,tblposts.PostUrl as url , tblposts.ptype as ptype , tblposts.link as link from tblposts left join tblcategory on tblcategory.id=tblposts.CategoryId left join  tblsubcategory on  tblsubcategory.SubCategoryId=tblposts.SubCategoryId where tblposts.Is_Active=1  and tblcategory.CategoryName='Circulars' order by tblposts.id desc  ")
      myresult = mycursor.fetchall()
      #st.write(myresult)
      for x in myresult:
        if int(x[9])==int(2):
          htmlstr1="<div class='alert alert-primary' role='alert'><a href='"+str(x[10])+" '>"+str(x[1])+"</a></div>"
          st.markdown(htmlstr1,unsafe_allow_html=True)
        elif int(x[9])==int(3):
          htmlstr1="<div class='alert alert-success' role='alert'><a href='https://swarnandhra.ac.in/swarnandhraexaminationportal/admin/postimages/"+str(x[2])+"'>"+str(x[1])+"</a></div>"
          st.markdown(htmlstr1,unsafe_allow_html=True)
        elif int(x[9])==int(1):
          st.info(str(x[1])+str(x[10]))
if choose == "Notifications":
      st.header("Notifications:")
      mycursor.execute("select tblposts.id as pid,tblposts.PostTitle as posttitle,tblposts.PostImage,tblcategory.CategoryName as category,tblcategory.id as cid,tblsubcategory.Subcategory as subcategory,tblposts.PostDetails as postdetails,tblposts.PostingDate as postingdate,tblposts.PostUrl as url , tblposts.ptype as ptype , tblposts.link as link from tblposts left join tblcategory on tblcategory.id=tblposts.CategoryId left join  tblsubcategory on  tblsubcategory.SubCategoryId=tblposts.SubCategoryId where tblposts.Is_Active=1  and tblcategory.CategoryName='Notifications' order by tblposts.id desc  ")
      myresult = mycursor.fetchall()
      #st.write(myresult)
      for x in myresult:
        if int(x[9])==int(2):
          htmlstr1="<div class='alert alert-primary' role='alert'><a href='"+str(x[10])+" '>"+str(x[1])+"</a></div>"
          st.markdown(htmlstr1,unsafe_allow_html=True)
        elif int(x[9])==int(3):
          htmlstr1="<div class='alert alert-success' role='alert'><a href='https://swarnandhra.ac.in/swarnandhraexaminationportal/admin/postimages/"+str(x[2])+"'>"+str(x[1])+"</a></div>"
          st.markdown(htmlstr1,unsafe_allow_html=True)
        elif int(x[9])==int(1):
          st.info(str(x[1])+str(x[10]))
if choose == "Contact":
  st.header("Contact Us:")
  st.success("SWARNANDHRA College of Engineering and Technology,Seetharampuram, Narsapur, Andhra Pradesh 534280, India")
  st.info("Email : info@swarnandhra.ac.in")
  st.warning("Phone: 9346610099 ,08821- 224705")