import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from settings import purpose, instructions, project_sections
from datetime import datetime


# Create the bulleted list using Markdown syntax
bullet_list = "\n".join([f"- {item}" for item in project_sections])

project_title = "Immunization Collaborative Supply Planning Strengthening Project"
tool_purpose = "Maturity Assessment Tool"
project_title_short = "ICSPS " + tool_purpose

st.set_page_config(
    page_title=project_title_short,
    layout="wide"
)


st.title(body=project_title)
st.subheader(tool_purpose)

st.title("Purpose")
st.markdown(
    f"This tool is used to assess the maturity of a country in terms of forecasting and supply planning for vaccines. For immunization forecasting and supply planning to be effective, it must be proactive rather than reactive. The tool looks at various characteristics in five broad categories for effective forecasting and supply planning: \n{
        bullet_list}"
)
st.markdown(" These characteristics holistically contribute to strengthening the forecasting and supply planning practices through the collaborative efforts of all relevant stakeholders in-country thus achieving the desired state of proactive forecasting and supply planning. The assessment results are used to map countries into 3 phases: ad-hoc forecasting and supply planning, reactive forecasting and supply planning, and proactive forecasting and supply planning, with the last being the ideal. Routine monitoring of vaccines by countries ensures that countries maintain adequate stocks of vaccines, align demand for vaccines with supply, and minimize stockouts or the need to destroy vaccines due to expiries.")

"---"

st.title("Instructions")
st.write(instructions)

"---"

with st.form("owner_info"):
    with st.expander("User Details"):
        country_being_assessed = st.text_input(
            "Enter Name of Country being assessed",
            key="country_being_assessed"
        )

        owner_name = st.text_input(
            "Name(s) of person(s) and organization(s) completing the assessment",
            key="owner",
            placeholder="Enter Period in YYYYQ format"
        )

        review_period = st.text_input(
            "Period of Review",
            key="period_of_review"
        )

        date_of_assessment = st.date_input(
            "Enter Date of Assessment in format YYYYMMDD:"
        )
    with st.expander("FSP Policies, Commitment & Political Will"):
        x_1_1 = st.radio(
            label="1 There is a multidisciplinary team responsible for forecasting and supply planning for vaccines. This can be any working group or unit responsible for FSP in the MOH",
            options=[
                "Absence of a team responsible for forecasting and supply planning for vaccines",
                "Forecasting and supply planning for vaccines is the responsibility of a few individuals within the MOH",
                "There is a multidisciplinary team that is tasked with the responsibility of forecasting and supply planning for vaccines"
            ],
            key="multidisciplinary_team_available",
            index=None
        )

        "---"
        x_1_2 = st.radio(
            label="2 Inclusion of all relevant stakeholders in forecasting and supply planning for vaccines in the country",
            options=[
                "Relevant stakeholders not included",
                "Limited inclusion of the relevant stakeholders",
                "All the relevant stakeholders are included "
            ],
            key="inclusion_of_relevant_stakeholders",
            index=None
        )

        "---"
        x_1_3 = st.radio(
            label="3 Existence of work plans, MoUs, or TORs for vaccine forecasting and supply planning (stand-alone or anchored on other documents)",
            options=[
                "Absence of ToR, MoU, or work plans for vaccine forecasting and supply planning",
                "ToR, MoU, or work plans for forecasting and supply planning for vaccines exist but have certain gaps",
                "Vaccine forecasting and supply planning prioritized in TOR, MoU, or work plans"
            ],
            key="existence_of_workplans",
            index=None
        )

        "---"
        x_1_4 = st.radio(
            label="4 The TOR covers the following key FSP functions and responsibilities listed; i) developing work plans, ii) organizing and completing FSP preparatory activities, iii) developing a forecast and supply plan, iv) ensuring FSP monitoring and implementation of a continuous improvement plan, v) leading standardization of FSP processes and training of members, vi) liaising with and leveraging skills and expertise available in other program areas to ensure alignment and integration; and, vii) supporting other innovative activities such as new vaccine introduction",
            options=[
                "The TORs does not cover any of the key FSP responsibilities",
                "The TORs cover at least two of the outlined FSP responsibilities",
                "The TORs cover at least four FSP responsibilities "
            ],
            key="tor_coverage",
            index=None
        )

        "---"
        x_1_5 = st.radio(
            label="5 The EPI program has a supply chain strategy that covers the following key technical areas of FSP; Preparatory activities for FSP (e.g. gathering and ratifying data assumptions and consultation meetings or workshops), Forecasting, Supply Planning, Pipeline Monitoring, and FSP performance monitoring",
            options=[
                "There is no SC strategy",
                "There is a SC strategy, but it does not cover any of the key technical areas of FSP ",
                "The SC strategy covers the key technical areas of FSP"
            ],
            key="epi_strategy",
            index=None
        )

        "---"
        x_1_6 = st.radio(
            label="6 Commitment from the relevant stakeholders toward forecasting and supply planning for vaccines",
            options=[
                "No commitment from the relevant stakeholders",
                "Limited commitment of the relevant stakeholders ",
                "Adequate commitment from relevant stakeholders"
            ],
            key="stakeholder_commitment",
            index=None
        )

        "---"
        x_1_7 = st.radio(
            label="7 Resources allocated for forecasting and supply planning-related tasks ",
            options=[
                "Resources are lacking for all FSP related tasks",
                "Resources are limited for FSP related tasks",
                "Adequate resources are available for all FSP related tasks"
            ],
            key="resource_allocation",
            index=None
        )

        "---"

        x_1_8 = st.text_area(
            label="Comments: ",
            height=20,
            placeholder="Enter your comments here...",
            key="fsp_comment"
        )

    with st.expander("Data"):

        x_2_1 = st.radio(
            label="8 Presence of a reliable system for collecting disaggregated data ",
            options=[
                "The country lacks a reliable system that captures disaggregated data",
                "The system for capturing disaggregated data has some gaps",
                "The country has a system that captures disaggregated data"
            ],
            key="presence_of_reliable_data_collection_system",
            index=None
        )

        "---"

        x_2_2 = st.radio(
            label="9 Access to relevant, quality, and disaggregated data (consumption data by product, dose and month, wastages - open and closed vial wastage, adjustments, expiries, etc.)",
            options=[
                "Disaggregated data is not available",
                "Limited access to disaggregated data, including potential delays in accessing",
                "There is seamless flow in accessing the disaggregated data "
            ],
            key="access_to_quality_disaggregated_data",
            index=None
        )

        "---"

        x_2_3 = st.radio(
            label="10 Accuracy of stock balances  ",
            options=[
                "Significant data discrepancy",
                "Partially accurate data",
                "The data matches the reality/is close to accurate "
            ],
            key="accuracy_of_data",
            index=None
        )

        "---"

        x_2_4 = st.radio(
            label="11 Data reporting practices (timeliness of reporting)",
            options=[
                "Poor data reporting practices that make the data unusable when needed",
                "Ad-hoc reporting and late updating of data",
                "Data is routinely and continuously updated and usable when needed"
            ],
            key="data_reporting",
            index=None
        )

        "---"

        x_2_5 = st.radio(
            label="12 Standardized tools for forecasting and supply planning are routinely used",
            options=[
                "There exists forecasting and supply planning tools but they are not used",
                "Only one of these tools (forecasting/supply planning) is used",
                "Both the forecasting and supply planning tools are used"
            ],
            key="tool_standardization",
            index=None
        )

        "---"

        x_2_6 = st.text_area(
            "Comments",
            height=20,
            key="x_2_comments"
        )
    with st.expander("Analysis"):
        x_3_1 = st.radio(
            label="13 Stock status is routinely assessed",
            options=[
                "Stock status is not assessed",
                "Stock status is assessed in an untimely manner",
                "Stock status is routinely assessed"
            ],
            key="stock_status_checked",
            index=None
        )

        "---"

        x_3_2 = st.radio(
            label="14 Methodology used for forecasting vaccines",
            options=[
                "Demographic/ wastage factor-based",
                "Consumption-based",
                "Vaccination session-based"

            ],
            key="vaccine_forecasting_methodology",
            index=None
        )

        "---"

        x_3_3 = st.radio(
            label="15 Data from decentralized levels (e.g., regions, districts, facilities) is used to develop the national forecast and supply plan",
            options=[
                "Decentralized level data is not used to develop national forecasts",
                "Partial use of decentralized level data in developing national forecasts",
                "Data from all decentralized levels is used to develop national forecasts"

            ],
            key="data_from_decentralized_levels",
            index=None
        )

        "---"

        x_3_4 = st.radio(
            label="16 Triangulation of data from different sources when developing national forecasts, e.g. EPI forecasting tool, stock management tool (SMT), District Vaccine Data Management Tool (DVD/MT), District Health Information System 2 (DHIS2), ViVa e.t.c",
            options=[
                "Data from one source used for forecasting",
                "Data from limited sources used for forecasting",
                "Data from all relevant and available sources is used for forecasting"

            ],
            key="data_triangulation",
            index=None
        )

        "---"

        x_3_5 = st.radio(
            label="17 Calculate and update forecasts based on updated data and discussions with stakeholders",
            options=[
                "Forecasts are not calculated or updated",
                "Forecasts are available but do not include up-to-date data or relevant stakeholders",
                "Accurate demand forecasts calculated and updated based on up-to-date data and in discussion with relevant stakeholders"

            ],
            key="forecast_calculation_and_update",
            index=None
        )

        # x_3_1 = st.radio(
        #     label="Stock status is routinely assessed",
        #     options=[
        #         "Stock status is not assessed",
        #         "Stock status is assessed in an untimely manner",
        #         "Stock status is routinely assessed"
        #     ],
        #     key="stock_status_checked",
        #     index=None
        # )

        # "---"

        # x_3_1 = st.radio(
        #     label="Stock status is routinely assessed",
        #     options=[
        #         "Stock status is not assessed",
        #         "Stock status is assessed in an untimely manner",
        #         "Stock status is routinely assessed"
        #     ],
        #     key="stock_status_checked",
        #     index=None
        # )

        # "---"

        # x_3_1 = st.radio(
        #     label="Stock status is routinely assessed",
        #     options=[
        #         "Stock status is not assessed",
        #         "Stock status is assessed in an untimely manner",
        #         "Stock status is routinely assessed"
        #     ],
        #     key="stock_status_checked",
        #     index=None
        # )

        # "---"

        # x_3_1 = st.radio(
        #     label="Stock status is routinely assessed",
        #     options=[
        #         "Stock status is not assessed",
        #         "Stock status is assessed in an untimely manner",
        #         "Stock status is routinely assessed"
        #     ],
        #     key="stock_status_checked",
        #     index=None
        # )

        # "---"

        # x_3_1 = st.radio(
        #     label="Stock status is routinely assessed",
        #     options=[
        #         "Stock status is not assessed",
        #         "Stock status is assessed in an untimely manner",
        #         "Stock status is routinely assessed"
        #     ],
        #     key="stock_status_checked",
        #     index=None
        # )

        # "---"

        # x_3_1 = st.radio(
        #     label="Stock status is routinely assessed",
        #     options=[
        #         "Stock status is not assessed",
        #         "Stock status is assessed in an untimely manner",
        #         "Stock status is routinely assessed"
        #     ],
        #     key="stock_status_checked",
        #     index=None
        # )

        # "---"

        # x_3_1 = st.radio(
        #     label="Stock status is routinely assessed",
        #     options=[
        #         "Stock status is not assessed",
        #         "Stock status is assessed in an untimely manner",
        #         "Stock status is routinely assessed"
        #     ],
        #     key="stock_status_checked",
        #     index=None
        # )

        "---"

    submitted_button_clicked = st.form_submit_button(
        "Submit")
if submitted_button_clicked:
    if any(not var for var in [country_being_assessed, owner_name, review_period, date_of_assessment,
                               x_1_1, x_1_2, x_1_3, x_1_4, x_1_5, x_1_6, x_1_7,
                               x_2_1, x_2_2, x_2_3, x_2_4, x_2_5, x_3_1, x_3_2, x_3_3, x_3_4, x_3_5]):
        st.error("Not Submitted! Please fill all fields")
        print("User is trying to submit an empty form")
    else:
        all_user_data = {
            "Name of Country being assessed": country_being_assessed,
            "Name(s) of person(s) and organization(s) completing the assessment": owner_name,
            "Period of Review": review_period,
            "Date of Assessment": date_of_assessment,
            "There is a multidisciplinary team responsible for forecasting and supply planning for vaccines. This can be any working group or unit responsible for FSP in the MOH": x_1_1,
            "Inclusion of all relevant stakeholders in forecasting and supply planning for vaccines in the country": x_1_2,
            "Existence of work plans, MoUs, or TORs for vaccine forecasting and supply planning (stand-alone or anchored on other documents)": x_1_3,
            "The TOR covers the following key FSP functions and responsibilities listed; i) developing work plans, ii) organizing and completing FSP preparatory activities, iii) developing a forecast and supply plan, iv) ensuring FSP monitoring and implementation of a continuous improvement plan, v) leading standardization of FSP processes and training of members, vi) liaising with and leveraging skills and expertise available in other program areas to ensure alignment and integration; and, vii) supporting other innovative activities such as new vaccine introduction": x_1_4,
            "The EPI program has a supply chain strategy that covers the following key technical areas of FSP; Preparatory activities for FSP (e.g. gathering and ratifying data assumptions and consultation meetings or workshops), Forecasting, Supply Planning, Pipeline Monitoring, and FSP performance monitoring": x_1_5,
            "Commitment from the relevant stakeholders toward forecasting and supply planning for vaccines": x_1_6,
            "Resources allocated for forecasting and supply planning-related tasks": x_1_7,
            "Presence of a reliable system for collecting disaggregated data": x_2_1,
            "Access to relevant, quality, and disaggregated data (consumption data by product, dose and month, wastages - open and closed vial wastage, adjustments, expiries, etc.)": x_2_2,
            "Accuracy of stock balances":  x_2_3,
            "Data reporting practices (timeliness of reporting)":  x_2_4,
            "Standardized tools for forecasting and supply planning are routinely used":  x_2_5,
            "Stock status is routinely assessed": x_3_1,
            "Methodology used for forecasting vaccines": x_3_2,
            "Data from decentralized levels (e.g., regions, districts, facilities) is used to develop the national forecast and supply plan": x_3_3,
            "Triangulation of data from different sources when developing national forecasts, e.g. EPI forecasting tool, stock management tool (SMT), District Vaccine Data Management Tool (DVD/MT), District Health Information System 2 (DHIS2), ViVa e.t.c": x_3_4,
            "Calculate and update forecasts based on updated data and discussions with stakeholders": x_3_5
        }

        all_user_data_df = pd.DataFrame.from_dict(
            all_user_data, orient="index", columns=["data"]).reset_index(names="field")

        print(all_user_data_df)
        st.success("Submitted Successfully!")
        st.header("Your Responses")
        st.table(
            all_user_data_df.dropna().set_index("field")
        )
