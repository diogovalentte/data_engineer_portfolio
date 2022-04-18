# Libraries
from pandas.io.formats.format import DataFrameFormatter
from streamlit_folium import folium_static
import pandas as pd
import numpy as np
import seaborn as sns
import streamlit as st
import sys


#! Add folder "src" as a package path
project_path = "Put/here/the/path/to/the/project's/root/folder/house_rocket_analysis"
sys.path.append(f'{project_path}/src/')
import visualization.maps as maps

#! App configuration
st.set_page_config(layout='wide')

@st.cache(allow_output_mutation=True)
def load_data(path):
    data = pd.read_csv(path)

    return data


# Pages definition
def sidebar():
    st.sidebar.title('Select Page')
    page_select = st.sidebar.selectbox( label='', options=['Final Reports', 'Maps'])

    return page_select


def page_final_reports(renamed_houses, recommended_houses):
    # Filter Recommended Houses to Buy DataFrame
    st.sidebar.title('Search for recommended home for purchase')
    id_input = str(st.sidebar.text_input(label='Enter the ID')).strip()  # Input ID to search house

    st.title('House Rocket Analysis')
    st.title('')

    st.title(f'There are {renamed_houses.shape[0]} properties available for purchase today.')
    st.dataframe(renamed_houses)

    st.header("Main considerations of the analysis.")

    st.markdown('* The variables with the highest positive correlation with Price are "Grade" and "Sqft living".')
    st.markdown('* Houses rated 8 or higher in the "Grid" (Quality of the building mateirais of the house) attribute have the best average price per rank and number of homes.')
    st.markdown('* The average price of renovated homes is 22% higher than unrenovated homes.')
    st.markdown('* The biggest correlation with Price and what can be added in a makeover is the bathroom and the amount of square feet of the house.')
    st.markdown('* The best season for re-selling homes is Spring.')

    st.header(
        """After these analyses, the recommended houses for House Rocket to buy follow the conditions:
    Places with grade of variable "Grid" (Quality of the building mateirais of the house) equal or greater than 8
    Houses with condition equal to or greater than 3
    Houses priced below the median price in your region (ZipCode)""")

    st.header("""The re-sale price of the after-purchased homes is based on the various "Total Avarage Price", which means the average value of the region's house prices (ZipCode) and the average price of the Season that the house was announced.
    If the purchase price of the house is higher than the "Total Avarage Price", then the suggested selling price will be the purchase price + 10%.

    If the purchase price of the house is less than the "Total Avarage Price", then the suggested selling price will be the purchase price + 30%.""")

    st.header("""A column has also been added in the table representing the recommended re-sale price and the profit from re-selling the house if it is renewed.
    If the house is renovated, the re-sale price and the after-sale profit will be 20% higher.
    """)

    st.title(f'After analysis, {recommended_houses.shape[0]} properties are recommended for purchase and re-sale.')

    st.subheader('New columns have also been added at the end of the table. They represent the recommended selling price of the houses, whether it has been renovated or not, in addition to the possible profit if sold at the recommended price.')
    st.text("")

    try:
        if not id_input:
            st.dataframe(recommended_houses)
        else:
            if int(id_input) in recommended_houses['ID'].values:
                st.dataframe(recommended_houses.loc[recommended_houses['ID'] == int(id_input)])
            else:
                st.error(
                    'Property with this ID is not recommended for purchase or there is no home with this ID.')
    except:
        st.error('ERROR: Input value is not a valid ID.')
    #finally:
        

    return None


def page_maps(renamed_houses, recommended_houses):
    # SideBar - - -
    st.sidebar.title('Filter Map')
    filter_data = st.sidebar.radio(label='Filter Houses', options=[
                                   'All houses', 'Recommended homes to buy'])

    # Filters - -
    if filter_data == 'Recommended homes to buy':
        st.title('Map of all recommended homes for purchase')
        st.header('')
        data = recommended_houses.copy()

    else:
        st.title('Map of all available houses')
        st.header('')
        data = renamed_houses.copy()

    # Map of density
    houses_map = maps.houses_map(data)
    folium_static(houses_map, width=1200, height=700)

    # Map with avarage price per region (ZipCode)
    st.title('Avarage Price per Region')
    avg_region = maps.price_per_region(renamed_houses)
    folium_static(avg_region, width=1200, height=700)


if __name__ == '__main__':
    path = f"{project_path}/data/interim/renamed_data.csv"
    renamed_houses = load_data(path)

    path = f"{project_path}/reports/data/final_houses_sale.csv"
    recommended_houses = load_data(path)

    page_select = sidebar()

    if page_select == 'Final Reports':
        page_final_reports(renamed_houses=renamed_houses, recommended_houses=recommended_houses)

    else:
        page_maps(renamed_houses=renamed_houses, recommended_houses=recommended_houses)
