import streamlit as st
from streamlit_option_menu import option_menu
from settings import purpose, instructions, project_sections, fsp_policies_section, data_section, analysis_section, forecasting_supply_planning_section, funding_adjustments_section
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

selected = option_menu(
    menu_title=None,
    options=[
        "Home Page",
        "Data Entry",

    ],
    icons=[
        'house', 'activity'
    ],
    menu_icon="list-nested",
    default_index=0,
    orientation="horizontal"
)


def calculate_total_score(scores):
    return sum(scores)


def determine_maturity_level(total_score):
    if total_score <= 62:
        return "Ad-hoc supply planning"
    elif total_score <= 88:
        return "Reactive supply planning"
    else:
        return "Proactive supply planning"


def main():

    if selected == "Home Page":

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

    else:
        with st.expander("Assessment info"):
            country_name = st.text_input("Name of Country being assessed")
            assessors_info = st.text_input(
                "Name(s) of person(s) and organization(s) completing the assessment")
            period_of_review = st.text_input("Period of Review")
            date_of_assessment = datetime.now()
            start_assessment = st.button(
                label="Start Assessment", key="start_assessment")

            if start_assessment:
                if not (country_name and assessors_info and period_of_review):
                    st.warning(
                        "Please fill in all assessment information before proceeding.")
                else:
                    st.success("Expand below to conduct assement")
                    print(country_name, assessors_info, period_of_review)
        with st.expander("FSP Policies, Commitment & Political Will"):
            fsp_policies_scores = fsp_policies_section()
        with st.expander("Data"):
            data_scores = data_section()
        with st.expander("Analysis"):
            analysis_scores = analysis_section()
        with st.expander("Forecasting and Supply Planning Activities"):
            forecasting_supply_planning_scores = forecasting_supply_planning_section()
        with st.expander("Funding and Adjustments of Forecasts and Supply Plans"):
            funding_adjustments_scores = funding_adjustments_section()

        st.divider()

        if st.button("Calculate Total Score"):
            total_score = calculate_total_score(
                fsp_policies_scores + data_scores + analysis_scores + forecasting_supply_planning_scores + funding_adjustments_scores)
            st.metric(label="Total Score", value=total_score)
            maturity_level = determine_maturity_level(total_score)
            st.markdown(f"# {assessors_info}'s Maturity Level for Review Period {
                        period_of_review}👇 :")
            st.markdown(f"## {maturity_level}")
            print(country_name, assessors_info,
                  period_of_review, funding_adjustments_scores, analysis_scores)


if __name__ == "__main__":
    main()
