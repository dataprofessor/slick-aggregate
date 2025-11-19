import streamlit as st
from streamlit_slickgrid import (
    slickgrid,
    Formatters,
    Filters,
    FieldType,
    StreamlitSlickGridFormatters,
)

st.set_page_config(layout="wide", page_title="Americas Data")

st.title("🌎 Americas Agricultural Data 2023")

# Sample data - North America children
north_america_children = [
    {
        "id": 102,
        "region": "North America",
        "country": "United States",
        "year": 2023,
        "area_ha": 157736800,
        "__parent": 101,
        "__depth": 1,
    },
    {
        "id": 103,
        "region": "North America",
        "country": "Canada",
        "year": 2023,
        "area_ha": 62420000,
        "__parent": 101,
        "__depth": 1,
    },
    {
        "id": 104,
        "region": "North America",
        "country": "Mexico",
        "year": 2023,
        "area_ha": 24500000,
        "__parent": 101,
        "__depth": 1,
    },
]

# Sample data - South America children
south_america_children = [
    {
        "id": 2,
        "region": "South America",
        "country": "Brazil",
        "year": 2023,
        "area_ha": 55642000,
        "__parent": 1,
        "__depth": 1,
    },
    {
        "id": 3,
        "region": "South America",
        "country": "Bolivia",
        "year": 2023,
        "area_ha": 5562567.6,
        "__parent": 1,
        "__depth": 1,
    },
    {
        "id": 4,
        "region": "South America",
        "country": "Paraguay",
        "year": 2023,
        "area_ha": 4561000,
        "__parent": 1,
        "__depth": 1,
    },
    {
        "id": 5,
        "region": "South America",
        "country": "Peru",
        "year": 2023,
        "area_ha": 3918431,
        "__parent": 1,
        "__depth": 1,
    },
    {
        "id": 6,
        "region": "South America",
        "country": "Venezuela, RB",
        "year": 2023,
        "area_ha": 2600000,
        "__parent": 1,
        "__depth": 1,
    },
    {
        "id": 7,
        "region": "South America",
        "country": "Colombia",
        "year": 2023,
        "area_ha": 2549300,
        "__parent": 1,
        "__depth": 1,
    },
    {
        "id": 8,
        "region": "South America",
        "country": "Uruguay",
        "year": 2023,
        "area_ha": 2199600,
        "__parent": 1,
        "__depth": 1,
    },
    {
        "id": 9,
        "region": "South America",
        "country": "Chile",
        "year": 2023,
        "area_ha": 1406900,
        "__parent": 1,
        "__depth": 1,
    },
    {
        "id": 10,
        "region": "South America",
        "country": "Ecuador",
        "year": 2023,
        "area_ha": 1028000,
        "__parent": 1,
        "__depth": 1,
    },
]

# Calculate total area for North America
na_total_area = sum(row["area_ha"] for row in north_america_children)

# Calculate percentage for each North American country
for row in north_america_children:
    row["percentage"] = (row["area_ha"] / na_total_area) * 100

# Calculate average percentage for North America parent
na_avg_percentage = sum(row["percentage"] for row in north_america_children) / len(north_america_children)

# Create North America parent row
north_america_parent = {
    "id": 101,
    "region": "North America",
    "country": "North America",
    "year": 2023,
    "area_ha": na_total_area,
    "percentage": na_avg_percentage,
    "__parent": None,
    "__depth": 0,
}

# Calculate total area for South America
sa_total_area = sum(row["area_ha"] for row in south_america_children)

# Calculate percentage for each South American country
for row in south_america_children:
    row["percentage"] = (row["area_ha"] / sa_total_area) * 100

# Calculate average percentage for South America parent
sa_avg_percentage = sum(row["percentage"] for row in south_america_children) / len(south_america_children)

# Create South America parent row
south_america_parent = {
    "id": 1,
    "region": "South America",
    "country": "South America",
    "year": 2023,
    "area_ha": sa_total_area,
    "percentage": sa_avg_percentage,
    "__parent": None,
    "__depth": 0,
}

# Combine all data: both parents and all children
data = [north_america_parent] + north_america_children + [south_america_parent] + south_america_children

# Define colors
red = "#ff4b4b"
green = "#21c354"
white = "#fafafa"
blue = "#1c83e1"

# Define columns
columns = [
    {
        "id": "country",
        "name": "Region/Country",
        "field": "country",
        "sortable": True,
        "minWidth": 200,
        "type": FieldType.string,
        "filterable": True,
        "formatter": Formatters.tree,
        "exportCustomFormatter": Formatters.treeExport,
    },
    {
        "id": "year",
        "name": "Year",
        "field": "year",
        "sortable": True,
        "minWidth": 100,
        "type": FieldType.number,
        "filterable": True,
    },
    {
        "id": "area_ha",
        "name": "Area (ha)",
        "field": "area_ha",
        "sortable": True,
        "minWidth": 180,
        "type": FieldType.number,
        "filterable": True,
        "formatter": StreamlitSlickGridFormatters.numberFormatter,
        "params": {
            "minDecimal": 0,
            "maxDecimal": 1,
            "thousandSeparator": ",",
            "numberSuffix": " ha",
        },
    },
    {
        "id": "percentage",
        "name": "Percentage",
        "field": "percentage",
        "sortable": True,
        "minWidth": 150,
        "type": FieldType.number,
        "filterable": True,
        "formatter": StreamlitSlickGridFormatters.barFormatter,
        "params": {
            "colors": [
                [5, white, green],
                [10, white, red],
                [100, white, red],
            ],
            "minDecimal": 2,
            "maxDecimal": 2,
            "numberSuffix": "%",
            "min": 0,
            "max": 100,
        },
    },
]

# Grid options
options = {
    "enableFiltering": True,
    "enableTreeData": True,
    "multiColumnSort": False,
    "autoResize": {
        "minHeight": 600,
    },
    "treeDataOptions": {
        "columnId": "country",
        "indentMarginLeft": 15,
        "initiallyCollapsed": False,
        "parentPropName": "__parent",
        "levelPropName": "__depth",
    },
}

# Display the grid
result = slickgrid(data, columns, options, key="americas_grid")

# Display summary statistics
st.divider()

st.subheader("📊 Summary Statistics")

col1, col2 = st.columns(2)

with col1:
    st.write("**North America**")
    st.metric("Countries", len(north_america_children))
    st.metric("Total Area", f"{na_total_area:,.1f} ha")
    st.metric("Avg Percentage", f"{na_avg_percentage:.2f}%")

with col2:
    st.write("**South America**")
    st.metric("Countries", len(south_america_children))
    st.metric("Total Area", f"{sa_total_area:,.1f} ha")
    st.metric("Avg Percentage", f"{sa_avg_percentage:.2f}%")

# Grand totals
st.divider()
grand_total_area = na_total_area + sa_total_area
total_countries = len(north_america_children) + len(south_america_children)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🌎 Total Countries", total_countries)

with col2:
    st.metric("🌎 Grand Total Area", f"{grand_total_area:,.1f} ha")

with col3:
    st.metric("🌎 Average Area per Country", f"{grand_total_area/total_countries:,.1f} ha")

st.caption("💡 Percentage shows each country's area as % of its region's total area")

# Show clicked row details
if result is not None:
    row_idx, col_idx = result
    clicked_data = data[row_idx]
    st.info(f"**Clicked Row Data:**")
    st.json(clicked_data)
    
    # Show if it's an aggregate row or detail row
    if clicked_data["__depth"] == 0:
        st.success("✅ This is an **aggregate row** (parent)")
    else:
        st.info("📍 This is a **detail row** (child)")
