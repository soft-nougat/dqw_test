# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 17:04:46 2020

Script with defined app, including styling.

@author: TNIKOLIC
"""

import streamlit as st
from PIL import Image
from helper_functions import *
from helper_functions import _get_session
from tabular_eda.structured_data import *

# app setup 
try:
    # remove any temp folders in the root
    #dirs = glob.glob("DQW_Temp*/")
    #for dir in dirs:
        #remove_folder_contents(dir)

    # get session id and create session specific folders
    id = _get_session()
    # now create a user specific folder
    temp_folder = 'DQW_Temp_'+ id
    
    if path.exists(temp_folder) == False:
        os.makedirs(temp_folder)
        os.makedirs(temp_folder+'/preprocessed_data')
        os.makedirs(temp_folder+'/synthetic_data')

    # create ss object
    if 'data' not in st.session_state:
        st.session_state.data = None
    if 'pr' not in st.session_state:
        st.session_state.pr = None
    if 'pdf_report' not in st.session_state:
        st.session_state.pdf_report = None
    if 'sw' not in st.session_state:
        st.session_state.sw = None
    if 'pipeline' not in st.session_state:
        st.session_state.pipeline = None  
    if 'pdf' not in st.session_state:
        st.session_state.pdf = None 

    # app design
    app_meta('🏗️')
    set_bg_hack('dqw_background.png')

    # set logo in sidebar using PIL
    logo = Image.open('logo.png')
    st.sidebar.image(logo, 
                     use_column_width=True)
    
    # hide warning for st.pyplot() deprecation
    st.set_option('deprecation.showPyplotGlobalUse', False)
    
    # Main panel setup
    display_app_header(main_txt='Data Quality Wrapper',
                       sub_txt='Clean, describe, visualise and select data for AI models')

    st.markdown("""---""")
    # provide options to user to navigate to other dqw apps
    app_section_button('Tabular Data Section 🏗️',
    '[Audio Data Section 🎶](https://share.streamlit.io/soft-nougat/dqw-ivves_audio/main/app.py)',
    '[Text Data Section 📚](https://share.streamlit.io/soft-nougat/dqw-ivves_text/main/app.py)',
    '[Image Data Section 🖼️](https://share.streamlit.io/soft-nougat/dqw-ivves_images/main/app.py)')
    st.markdown("""---""")
    
    structured_data_app(temp_folder)
    remove_folder_contents(temp_folder)

except KeyError:
    st.error("Please select a key value from the dropdown to continue.")
    remove_folder_contents(temp_folder)
    
except ValueError:
    st.error("Oops, something went wrong. Please check previous steps for inconsistent input.")
    remove_folder_contents(temp_folder)
    
except TypeError:
    st.error("Oops, something went wrong. Please check previous steps for inconsistent input.")
    remove_folder_contents(temp_folder)

except RuntimeError:
    st.error("Oops, something went wrong. Please check previous steps for inconsistent input.")
    remove_folder_contents(temp_folder)
