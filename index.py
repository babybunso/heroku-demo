import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

st.title('MY DS Cheatsheet')
st.set_option('deprecation.showPyplotGlobalUse', False)

topic = st.sidebar.radio("Topics", ('Data Visualization', 'Git', 'KMeans', 'Heroku Commands', 'Conda Virtualenv',))

if topic == 'Data Visualization':
    st.markdown('<hr>', unsafe_allow_html=True)
    
    viz_option = st.selectbox('Graph Type:', ('Bar', 'Line'))
    if viz_option == 'Bar':
        sns.set_theme(style="whitegrid")
        tips = sns.load_dataset("tips")

        plt.figure(figsize=(15,8))
        ax = sns.barplot(x="day", y="total_bill", data=tips, ci = None)
        ax.set_title('Total Bill Per Day')
        ax.set(xlabel='Total Bill', ylabel='Day')
        st.pyplot()
        
        st.markdown("<a href='https://github.com/rheyannmagcalas/cheatsheet/blob/b6a317559757a9a3ca2343dbb93f1ad9f085634d/visualizations/visualizations.py#L1'></a>", unsafe_allow_html=True)
#     plt.show()

elif topic == 'Git':
    st.markdown('<hr>', unsafe_allow_html=True)
    st.markdown('<table style="font-size:11px">'\
                '<thead><tr><th>Command</th><th>Command</th></tr></thead>'\
                '<tbody><td>git status</td><td>Displays the state of the working directory</td></tbody>'\
                '<tbody><td>git add your_filename</td><td>Adds a change in the working directory to the staging area.</td></tbody>'\
                '<tbody><td>git commit -m your_message</td><td>Saving Changes to local repository</td></tbody>'\
                '<tbody><td>git push origin your_branch</td><td>Command used to upload local repository to a remote repository</td></tbody>'\
                '<tbody><td>git pull origin your_branch</td><td>Command used to fetch and download content from a remote repository.</td></tbody>'\
                '<tbody><td>git stash</td><td>Command to go back to a clean working directory.</td></tbody>'\
                '<tbody><td>git log</td><td>View Information to previous commits.</td></tbody>'\
                '<tbody><td>git checkout your_commit_id</td><td>Switch branches or restore working tree files</td></tbody>'\
                '</table>', unsafe_allow_html=True)
elif topic == 'KMeans':
    st.markdown('<hr>', unsafe_allow_html=True)
    
elif topic == 'Heroku Commands':
    st.markdown('<hr>', unsafe_allow_html=True)
    st.text('Make sure you are inside the repository')
    st.markdown('<table style="font-size:11px">'\
                '<thead><tr><th>Usage</th><th>Command</th></tr></thead>'\
                '<tbody><td>Login</td><td>heroku login -i</td></tbody>'\
                '<tbody><td>Create Instance</td><td>heroku create</td></tbody>'\
                '<tbody><td>Install your Code</td><td>git push heroku your_branch_name</td></tbody>'\
                '<tbody><td>Scaling your app to one dyno</td><td>heroku ps:scale web=1</td></tbody>'\
                '<tbody><td>Checking logs</td><td>heroku logs --tail</td></tbody>'\
                '<tbody><td>Rename Applications</td><td>heroku apps:rename newname --app oldname</td></tbody>'\
                '</table>', unsafe_allow_html=True)

    
elif topic == 'Conda Virtualenv':
    st.markdown('<hr>', unsafe_allow_html=True)
    st.subheader('What is virtualenv?')
    st.write('Virtualenv is a tool to create isolated Python environments. ')
    
    st.subheader('Steps to Create and Use Virtualenv:')
    st.markdown('<b>1. Create Environment:</b> <br> conda create -n <env_name> python=<python_version>', unsafe_allow_html=True)
    st.markdown('<b>2. Check if Environment is Created:</b> <br> conda info --envs', unsafe_allow_html=True)
    st.markdown('<b>3. Activate Environment:</b> <br>  conda activate <env_name>', unsafe_allow_html=True)
    st.markdown('<b>4. Open Jupyter Notebook</b> <br>', unsafe_allow_html=True)
    
    st.markdown('<hr>', unsafe_allow_html=True)
    st.markdown('<b>Save Installed Libraries:</b> pip freeze >> requirements.txt', unsafe_allow_html=True)
    st.markdown('<b>Install Multiple Libraries:</b> pip install -r requirements.txt', unsafe_allow_html=True)
    
    st.markdown('<hr>', unsafe_allow_html=True)
    st.markdown('<b>Stop Enviroment:</b>&nbsp;&nbsp;&nbsp;&nbsp;conda deactivate', unsafe_allow_html=True)
    st.markdown('<b>Delete Enviroment:</b>&nbsp;conda remove -n <env_name> --all', unsafe_allow_html=True)
    
        
        

# import streamlit as st

# def get_user_name():
#     return 'John'

# with st.echo():
#     # Everything inside this block will be both printed to the screen
#     # and executed.

#     def get_punctuation():
#         return '!!!'

#     greeting = "Hi there, "
#     value = get_user_name()
#     punctuation = get_punctuation()

    #st.write(greeting, value, punctuation)

# And now we're back to _not_ printing to the screen
# foo = 'bar'
# st.write('Done!')

