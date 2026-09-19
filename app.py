import streamlit as st
import pandas as pd
from datetime import datetime
import json
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
from streamlit_local_storage import LocalStorage

from dependencies import (
    instructions, project_sections,
    fsp_policies_section, data_section,
    analysis_section, forecasting_supply_planning_section,
    funding_adjustments_section,
    gesi_section,
    countries, review_periods,
    append_to_sheet, default_response_note,)

# Create the bulleted list using Markdown syntax
bullet_list = "\n".join([f"- {item}" for item in project_sections])
project_title = "Immunization Collaborative Supply Planning Strengthening Project"
tool_purpose = "[Maturity Assessment Tool](https://docs.google.com/document/d/1mqzwH8rl5hnuttw8Lf9z4Sh_w0P_vv5t/edit)"
project_title_short = "ICSPS " + tool_purpose

st.set_page_config(
    page_title=project_title_short,
    layout="wide"
)

# Initialize Local Storage component
localS = LocalStorage()

selected = option_menu(
    menu_title=None,
    options=[
        "Home Page",
        "Data Entry"
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
            f"This tool is used to assess the maturity of a country in terms of forecasting and supply planning for vaccines. For immunization forecasting and supply planning to be effective, it must be proactive rather than reactive. The tool looks at various characteristics in five broad categories for effective forecasting and supply planning:"
        )
        st.markdown(bullet_list)
        st.markdown(" These characteristics holistically contribute to strengthening the forecasting and supply planning practices through the collaborative efforts of all relevant stakeholders in-country thus achieving the desired state of proactive forecasting and supply planning. The assessment results are used to map countries into 3 phases: ad-hoc forecasting and supply planning, reactive forecasting and supply planning, and proactive forecasting and supply planning, with the last being the ideal. Routine monitoring of vaccines by countries ensures that countries maintain adequate stocks of vaccines, align demand for vaccines with supply, and minimize stockouts or the need to destroy vaccines due to expiries." )
                 
        st.markdown ("The tool also considers gender, equity and social inclusion (GESI), which refers to the intentional consideration of how different groups—such as women, men, adolescents,people with dissabilities and those in remote or underserved areas experience access to health services including Immunization. In the context of FSP,intergrating a GESI lens does not expand the technical mandate of FSP, which remains focused on estimating vaccine needs and planning for timely and adequate supply. Rather it strengthens the quality and responsiveness of FSP by improving accuracy of assumptions, supporting equity aware adjustments,and helping ensure no population is left behind.GESI intergration in FSP includes the use of dissagregated data(e.g.,by sex,age,geography)where available,meaningful cordination with technical GESI expertise to inform planning and international efforts to ensure divrse representation within FSP Teams.These componenents help ensure that forecasts and supply plans are based on a realistic understanding of who is being reached,who is not, and why without asking the FSP team to lead or fund service delivery or outreach efforts. Instead, GESI intergration enables the FSP to better align with broader equity goals while staying fully within its technical scope. ")
        st.divider()
        st.title("Instructions")
        st.write(instructions)
        st.write(f":red[{default_response_note}]")
        st.divider()
        st.image("www/combined_logos_1.png",
                 use_container_width=True, clamp=True, width=250)
        st.divider()
    else:
        st.divider()

        # Initialize a dynamic form key
        if "form_key" not in st.session_state:
            st.session_state["form_key"] = "form_0"

        # Check if a clear was requested on the PREVIOUS click
        if st.session_state.get("clear_requested"):
            localS.setItem("icsps_form_draft", {})
            
            # Clear all answers from Streamlit's internal memory
            for key in list(st.session_state.keys()):
                if key != "clear_requested":
                    del st.session_state[key]
            
            st.toast("Draft cleared! Refreshing...", icon="🔄")
            
            # Inject a Javascript auto-refresh to force the frontend visual cache to clear
            components.html(
                """
                <script>
                setTimeout(function() {
                    window.parent.location.reload();
                }, 500);
                </script>
                """,
                height=0
            )
            st.stop()

        # Load draft data on page initialization (ONLY if it has data and wasn't just cleared)
        saved_draft = localS.getItem("icsps_form_draft")
        if saved_draft and not st.session_state.get("draft_loaded") and not st.session_state.get("clear_requested"):
            try:
                draft_data = saved_draft if isinstance(saved_draft, dict) else json.loads(saved_draft)
                if draft_data: 
                    for k, v in draft_data.items():
                        st.session_state[k] = v
                st.session_state["draft_loaded"] = True
                st.rerun()
            except Exception as e:
                pass

        # === START OF BATCH FORM ===
        with st.form(st.session_state["form_key"]):
            st.subheader("Required fields")
            country_name = st.selectbox(
                "Name of Country being assessed", countries, placeholder="Choose country", key="country_name")
            assessors_name = st.text_input(
                "Name", placeholder="Enter your name", key="assessors_name")
            assessors_affiliation = st.text_input(
                "Organization", placeholder="Enter your organization's name", key="assessors_affiliation"
            )
            period_of_review = st.selectbox(
                "Period of Review", review_periods, placeholder="Choose the period of review", key="period_of_review")
            date_of_assessment = datetime.now()
            st.divider()
            
            with st.expander("FSP Policies, Commitment & Political Will"):
                def columns_adder(df, section):
                    df["country"] = country_name
                    df["assessors_name"] = assessors_name
                    df["assessors_affiliation"] = assessors_affiliation
                    df["period_of_review"] = period_of_review
                    df["date_of_assessment"] = date_of_assessment
                    df["section"] = section
                    return df
                fsp_policies_section_df = columns_adder(
                    df=fsp_policies_section(),
                    section="FSP Policies, Commitment & Political Will"
                )
            with st.expander("Data"):
                data_section_df = columns_adder(
                    df=data_section(),
                    section="Data"
                )
            with st.expander("Analysis"):
                analysis_section_df = columns_adder(
                    df=analysis_section(),
                    section="Analysis"
                )
            with st.expander("Forecasting and Supply Planning Activities"):
                forecasting_supply_planning_section_df = columns_adder(
                    df=forecasting_supply_planning_section(),
                    section="Forecasting and Supply Planning Activities"
                )
            with st.expander("Funding and Adjustments of Forecasts and Supply Plans"):
                funding_adjustments_section_df = columns_adder(
                    df=funding_adjustments_section(),
                    section="Funding and Adjustments of Forecasts and Supply Plans"
                )
            with st.expander("Gender Equity and Social Inclusion"):
                gesi_section_df = columns_adder(
                    df=gesi_section(),
                    section="Gender Equity and Social Inclusion"
                )
            with st.expander("Participants List"):
                participants_list = st.text_area(
                    " ", placeholder="Please fill the name of each person and their organisation in brackets separated with a comma. e.g. Jane Doe (JSI), John Doe (CHAI)",
                    key="participants_list"
                )
            
            st.divider()
            
            # Form submit buttons
            col1, col2 = st.columns([2, 5])
            with col1:
                update_btn = st.form_submit_button("💾 Save Draft", type="primary")
            with col2:
                clear_btn = st.form_submit_button("🗑️ Clear Form")
        # === END OF BATCH FORM ===

        # Handle Clear Button (Sets flag and instantly reruns to trigger step 2 above)
        if clear_btn:
            st.session_state["clear_requested"] = True
            st.rerun()

        # Handle Save Button
        if update_btn:
            draft_keys = [
                "country_name", "assessors_name", "assessors_affiliation", "period_of_review", "participants_list",
                "1", "2", "3", "4", "5", "6", "7", "fsp",
                "8", "9", "10", "11", "12", "data",
                "13", "14", "15", "16", "17", "18", "20", "21", "22", "analysis",
                "23", "24", "25", "26", "27", "28", "29", "30", "forecasting_supply_planning",
                "34", "35", "36", "37", "funding_adjst",
                "38", "39", "40", "41", "42", "43", "44", "45"
            ]
            draft_data = {k: st.session_state[k] for k in draft_keys if k in st.session_state}
            localS.setItem("icsps_form_draft", draft_data)
            st.toast("Draft successfully saved", icon="✅")

        # Process and show results (Outside the form, updates only when submitted)
        st.divider()
        with st.expander("View Results Table", expanded=True):
            all_data = pd.concat([
                fsp_policies_section_df, data_section_df, analysis_section_df,
                forecasting_supply_planning_section_df, funding_adjustments_section_df, gesi_section_df
            ], axis=0)
            st.dataframe(all_data.reset_index(drop=True), hide_index=True)
            total_score = all_data['score'].sum(skipna=True)
            
        maturity_level = determine_maturity_level(total_score)
        all_data["maturity_level"] = maturity_level
        all_data["participants"] = participants_list
        
        st.markdown("### Your maturity level is:")
        st.markdown(f"#### {maturity_level}")
        st.metric(label="Total Maturity Score", value=total_score)
        
        # Standard button for final Google Sheets submission
        submit_data = st.button(
            label="Final Submit to Database", key="submit_assessment_df", type="primary")
            
        validate_data = [country_name, assessors_name,
                         assessors_affiliation, period_of_review]
                         
        if submit_data:
            if any(not item for item in validate_data):
                st.error("Required fields cannot be Empty. Please update the form first.")
            else:
                try:
                    append_to_sheet(all_data, "icsps_data_for_pbi")
                except Exception as e:
                    print(e)
                    st.error("Could not save Data")
                else:
                    st.success("Successfully submitted!🔔")
                    print("Successfully submitted!🔔")
                    localS.setItem("icsps_form_draft", {}) 

if __name__ == "__main__":
    main()