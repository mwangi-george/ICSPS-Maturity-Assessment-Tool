import pandas as pd
import streamlit as st
import os
import gspread
from google.oauth2.service_account import Credentials
from gspread_dataframe import set_with_dataframe
from google.oauth2 import service_account
from dotenv import load_dotenv


load_dotenv()
project_sections = [
    "FSP Policies, Commitment & Political Will",
    "Data",
    "Analysis",
    "Forecasting and Supply Planning Activities",
    "Funding and Adjustments of Forecasts and Supply Plans"
]


purpose = """
This tool is used to assess the maturity of a country in terms of forecasting and supply planning for vaccines.
For immunization forecasting and supply planning to be effective, it must be proactive rather than reactive. 
The tool looks at various characteristics in five broad categories for effective forecasting and supply planning: 
    
    1. FSP Policies, Commitment and Political Will, 
    2. Data, 
    3. Analysis, 
    4. Forecasting, and Supply Planning Activities, 
    5. and Funding and Adjustments of Forecasts and Supply Plans. 

These characteristics holistically contribute to strengthening the forecasting and supply planning practices through the collaborative efforts of all relevant stakeholders in-country thus achieving the desired state of proactive forecasting and supply planning. 
The assessment results are used to map countries into 3 phases: ad-hoc forecasting and supply planning, reactive forecasting and supply planning, and proactive forecasting and supply planning, with the last being the ideal. 
Routine monitoring of vaccines by countries ensures that countries maintain adequate stocks of vaccines, align demand for vaccines with supply, and minimize stockouts or the need to destroy vaccines due to expiries.
"""

instructions = """
The tool is to be completed by country EPI teams that are part of the ICSPS initiative. 
The assessment will be completed every quarter, to show progress over time. 
The assessment results will be used by countries to identify and prioritize areas for strengthening, 
using which the teams will develop action plans for implementation. 

For each of the questions, please select the answer that best describes the status in the country, 
particularly the EPI Team, the National Logistics Working Group for Immunization, or any other task force/body in the country that is responsible for supply and demand planning for vaccines within the country.  

If you have any key comments, please provide them in the sections provided at the bottom of each category in the tool.

"""


questions = [
    "There is a multidisciplinary team responsible for forecasting and supply planning for vaccines. This can be any working group or unit responsible for FSP in the MOH",
    "Inclusion of all relevant stakeholders in forecasting and supply planning for vaccines in the country",
    "Existence of work plans, MoUs, or TORs for vaccine forecasting and supply planning (stand-alone or anchored on other documents)",
    "The TOR covers the following key FSP functions and responsibilities listed; i) developing work plans, ii) organizing and completing FSP preparatory activities, iii) developing a forecast and supply plan, iv) ensuring FSP monitoring and implementation of a continuous improvement plan, v) leading standardization of FSP processes and training of members, vi) liaising with and leveraging skills and expertise available in other program areas to ensure alignment and integration; and, vii) supporting other innovative activities such as new vaccine introduction",
    "The EPI program has a supply chain strategy that covers the following key technical areas of FSP; Preparatory activities for FSP (e.g. gathering and ratifying data assumptions and consultation meetings or workshops), Forecasting, Supply Planning, Pipeline Monitoring, and FSP performance monitoring",
    "Commitment from the relevant stakeholders toward forecasting and supply planning for vaccines",
    "Resources allocated for forecasting and supply planning-related tasks",
    "FSP Policies, Commitment & Political Will Comments",
    "Presence of a reliable system for collecting disaggregated data",
    "Access to relevant, quality, and disaggregated data (consumption data by product, dose and month, wastages - open and closed vial wastage, adjustments, expiries, etc.)",
    "Accuracy of stock balances",
    "Data reporting practices (timeliness of reporting)",
    "Standardized tools for forecasting and supply planning are routinely used",
    "Data Comments",
    "Stock status is routinely assessed",
    "Methodology used for forecasting vaccines",
    "Data from decentralized levels (e.g., regions, districts, facilities) is used to develop the national forecast and supply plan",
    "Triangulation of data from different sources when developing national forecasts, e.g. EPI forecasting tool, stock management tool (SMT), District Vaccine Data Management Tool (DVD/MT), District Health Information System 2 (DHIS2), ViVa e.t.c",
    "Calculate and update forecasts based on updated data and discussions with stakeholders",
    "Forecasts and supply plans developed (determination of what needs to be ordered by whom and when)",
    "Forecasting and supply plan report (or supply plan) cover key components of the quantification report (or supply plan), i.e. Forecasting assumptions and considerations, Forecasted quantities, Quantities required to fill the supply pipeline, funding requirement/costs, shipment schedules, including specific lead times where applicable",
    "Conduct scenario monitoring",
    "Ability to estimate the potential for vaccine expiry",
    "Analysis Comments",
    "Forecasting and supply planning activities included in the EPI work plans",
    "Forecasting and supply planning activities are inclusive of all relevant stakeholders (including implementing partners and donors)",
    "Regular and routine supply planning meetings scheduled (ideally quarterly at minimum)",
    "Forecasting and supply planning meetings review previous actions and recommendations",
    "Flexible to convene ad-hoc meetings to respond to emerging supply planning (SP) needs",
    "Decisions made in a timely and well-coordinated manner",
    "Decisions are based on evidence",
    "Meetings address supply planning risks",
    "Forecasting and Supply Planning Activities Comments",
    "Results of forecasting and supply planning reports are communicated to all relevant stakeholders",
    "Recommended adjustments are communicated to all relevant stakeholders",
    "Recommended adjustments are made in a timely and complete fashion",
    "Funding is available in a timely manner for total commodity requirement",
    "Funding is available to implement the recommended supply plan adjustments in a timely manner",
    "Funding and Adjustments of Forecasts and Supply Plans Comments"
]

questions_df = pd.DataFrame(questions, columns=["questions"])


def fsp_policies_section():
    st.subheader(questions[0])
    team_options = [
        "Absence of a team responsible for forecasting and supply planning for vaccines",
        "Forecasting and supply planning for vaccines is the responsibility of a few individuals within the MOH",
        "There is a multidisciplinary team that is tasked with the responsibility of forecasting and supply planning for vaccines"
    ]
    team_status = st.radio("Select team status:", team_options, key="1")

    st.subheader(questions[1])
    stakeholders_options = [
        "Relevant stakeholders not included",
        "Limited inclusion of stakeholders",
        "All relevant stakeholders included"
    ]
    stakeholders_status = st.radio(
        "Select stakeholders inclusion status:", stakeholders_options, key="2")

    st.subheader(questions[2])
    plans_options = [
        "Absence of ToR, MoU, or work plans for vaccine forecasting and supply planning",
        "ToR, MoU, or work plans for forecasting and supply planning for vaccines exist but have certain gaps",
        "Vaccine forecasting and supply planning prioritized in TOR, MoU, or work plans"

    ]
    plans_status = st.radio("Select work plans status:",
                            plans_options, key="3")

    st.subheader(questions[3])
    tor_options = [
        "The TORs does not cover any of the key FSP responsibilities",
        "The TORs cover at least two of the outlined FSP responsibilities",
        "The TORs cover at least four FSP responsibilities"
    ]
    tor_status = st.radio("Select TORs status:", tor_options, key="4")

    st.subheader(questions[4])
    strategy_options = [
        "There is no SC strategy",
        "There is a SC strategy, but it does not cover any of the key technical areas of FSP",
        "The SC strategy covers the key technical areas of FSP"
    ]
    strategy_status = st.radio(
        "Select SC strategy status:", strategy_options, key="5")

    st.subheader(questions[5])
    commitment_options = [
        "No commitment from the relevant stakeholders",
        "Limited commitment of the relevant stakeholders",
        "Adequate commitment from relevant stakeholders"
    ]
    commitment_status = st.radio(
        "Select commitment status:", commitment_options, key="6")

    st.subheader(questions[6])
    resources_options = [
        "Resources are lacking for all FSP related tasks",
        "Resources are limited for FSP related tasks",
        "Adequate resources are available for all FSP related tasks"
    ]
    resources_status = st.radio(
        "Select resources status:", resources_options, key="7")
    st.subheader(questions[7])
    section_1_comment = st.text_area("Provide comments here:", key="fsp")

    # Create a data frame with the responses
    responses = [
        team_status, stakeholders_status,
        plans_status, tor_status, strategy_status,
        commitment_status, resources_status,
        section_1_comment
    ]
    answers_df = pd.DataFrame(responses, columns=["answer"])
    questions_answers_df = pd.concat(
        [questions_df[0:8].reset_index(drop=True), answers_df], axis=1)
    scores = [
        team_options.index(team_status) + 1,
        stakeholders_options.index(stakeholders_status) + 1,
        plans_options.index(plans_status) + 1,
        tor_options.index(tor_status) + 1,
        strategy_options.index(strategy_status) + 1,
        commitment_options.index(commitment_status) + 1,
        resources_options.index(resources_status) + 1
    ]
    scores_df = pd.DataFrame(scores, columns=["score"])

    combined_df = pd.concat([questions_answers_df, scores_df], axis=1)
    return combined_df


def data_section():
    st.subheader(questions[8])
    disaggregated_options = [
        "The country lacks a reliable system",
        "The system has some gaps",
        "The country has a reliable system"
    ]
    disaggregated_status = st.radio(
        "Select disaggregated data status:", disaggregated_options, key="8")

    st.subheader(questions[9])
    access_options = ["Disaggregated data is not available",
                      "Limited access to disaggregated data", "Seamless flow in accessing disaggregated data"]
    access_status = st.radio(
        "Select data access status:", access_options, key="9")

    st.subheader(questions[10])
    stock_options = ["Significant data discrepancy",
                     "Partially accurate data", "Data matches reality/is close to accurate"]
    stock_status = st.radio(
        "Select stock balances status:", stock_options, key="10")

    st.subheader(questions[11])
    reporting_options = ["Poor data reporting practices",
                         "Ad-hoc reporting and late updating", "Data is routinely and continuously updated"]
    reporting_status = st.radio(
        "Select reporting practices status:", reporting_options, key="11")

    st.subheader(questions[12])
    tools_options = ["Tools exist but not used", "Only one tool used",
                     "Both forecasting and supply planning tools used"]
    tools_status = st.radio("Select tools status:", tools_options, key="12")

    st.subheader(questions[13])
    comments = st.text_area("Provide comments here:", key="data")

    responses = [
        disaggregated_status, access_status, stock_status, reporting_status, tools_status, comments
    ]

    answers_df = pd.DataFrame(responses, columns=["answer"])
    questions_answers_df = pd.concat(
        [questions_df[8:14].reset_index(drop=True), answers_df], axis=1)
    scores = [
        disaggregated_options.index(disaggregated_status) + 1,
        access_options.index(access_status) + 1,
        stock_options.index(stock_status) + 1,
        reporting_options.index(reporting_status) + 1,
        tools_options.index(tools_status) + 1
    ]

    scores_df = pd.DataFrame(scores, columns=["score"])

    combined_df = pd.concat([questions_answers_df, scores_df], axis=1)

    return combined_df


def analysis_section():
    st.subheader(questions[14])
    stock_status_options = ["Stock status not assessed",
                            "Untimely assessment of stock status", "Routinely assessed stock status"]
    stock_status = st.radio(
        "Select stock status assessment:", stock_status_options, key="13")

    st.subheader(questions[15])
    forecasting_method_options = [
        "Demographic/wastage factor-based", "Consumption-based", "Vaccination session-based"]
    forecasting_method = st.radio(
        "Select forecasting methodology:", forecasting_method_options, key="14")

    st.subheader(questions[16])
    decentralized_data_options = ["Decentralized data not used for national forecasts",
                                  "Partial use of decentralized data", "Data from all levels used for national forecasts"]
    decentralized_data = st.radio(
        "Select use of decentralized data:", decentralized_data_options, key="15")

    st.subheader(questions[17])
    triangulation_options = ["Data from one source used",
                             "Data from limited sources used", "Data from all relevant sources used"]
    triangulation = st.radio(
        "Select data triangulation status:", triangulation_options, key="16")

    st.subheader(questions[18])
    update_forecasts_options = ["Forecasts not calculated or updated",
                                "Forecasts available but not updated with current data", "Accurate forecasts updated based on current data"]
    update_forecasts = st.radio(
        "Select update forecasts status:", update_forecasts_options, key="17")

    st.subheader(questions[19])
    determine_orders_options = ["Unable to determine accurate orders",
                                "Some accuracy in determining orders", "Accurate determination of orders"]
    determine_orders = st.radio(
        "Select determine orders status:", determine_orders_options, key="18")

    st.subheader(questions[20])
    plan_coverage_options = ["Reports cover 0-2 key components",
                             "Reports cover at least 3 key components", "Reports cover all 5 key components"]
    plan_coverage = st.radio(
        "Select plan coverage status:", plan_coverage_options, key="20")

    st.subheader(questions[21])
    scenario_monitoring_options = ["Scenario monitoring not conducted",
                                   "Poorly conducted scenario monitoring", "Well-conducted scenario monitoring"]
    scenario_monitoring = st.radio(
        "Select scenario monitoring status:", scenario_monitoring_options, key="21")

    st.subheader(questions[22])
    expiry_estimation_options = ["Inability to estimate vaccine expiry",
                                 "Limited ability to estimate expiry", "Ability to estimate expiry"]
    expiry_estimation = st.radio(
        "Select expiry estimation status:", expiry_estimation_options, key="22")

    st.subheader(questions[23])
    comments = st.text_area("Provide comments here:")

    responses = [
        stock_status, forecasting_method, decentralized_data,
        triangulation, update_forecasts, determine_orders,
        plan_coverage, scenario_monitoring, expiry_estimation, comments
    ]

    answers_df = pd.DataFrame(responses, columns=["answer"])
    questions_answers_df = pd.concat(
        [questions_df[14:24].reset_index(drop=True), answers_df], axis=1)
    scores = [
        stock_status_options.index(stock_status) + 1,
        forecasting_method_options.index(forecasting_method) + 1,
        decentralized_data_options.index(decentralized_data) + 1,
        triangulation_options.index(triangulation) + 1,
        update_forecasts_options.index(update_forecasts) + 1,
        determine_orders_options.index(determine_orders) + 1,
        plan_coverage_options.index(plan_coverage) + 1,
        scenario_monitoring_options.index(scenario_monitoring) + 1,
        expiry_estimation_options.index(expiry_estimation) + 1
    ]

    scores_df = pd.DataFrame(scores, columns=["score"])

    combined_df = pd.concat([questions_answers_df, scores_df], axis=1)

    return combined_df


def forecasting_supply_planning_section():
    st.subheader(questions[24])
    work_plans_options = ["Forecasting and supply planning activities not included",
                          "Partially included in EPI work plans", "Adequately included in EPI work plans"]
    work_plans_status = st.radio(
        "Select inclusion in EPI work plans status:", work_plans_options, key="23")

    st.subheader(questions[25])
    stakeholders_options = ["Key stakeholders not included",
                            "Limited participation by relevant stakeholders", "All relevant stakeholders included"]
    stakeholders_status = st.radio(
        "Select stakeholders inclusion status:", stakeholders_options, key="24")

    st.subheader(questions[26])
    meetings_options = ["Meetings not being held",
                        "Irregular/ad-hoc meetings", "Regularly scheduled meetings"]
    meetings_status = st.radio(
        "Select supply planning meetings status:", meetings_options, key="25")

    st.subheader(questions[27])
    review_options = ["Meetings do not review past actions and recommendations",
                      "Partial review/addressing of past actions and recommendations", "Full review and addressing of past actions and recommendations"]
    review_status = st.radio("Select review status:", review_options, key="26")

    st.subheader(questions[28])
    flexibility_options = ["Lack of flexibility to convene ad hoc meetings",
                           "Limited flexibility to convene ad-hoc meetings", "Flexible to convene ad-hoc meetings"]
    flexibility_status = st.radio(
        "Select flexibility status:", flexibility_options, key="27")

    st.subheader(questions[29])
    decisions_options = ["Decisions not made",
                         "Decisions made in an untimely manner", "Decisions made in a timely manner"]
    decisions_status = st.radio(
        "Select decisions status:", decisions_options, key="28")

    st.subheader(questions[30])
    evidence_options = ["Decisions not informed by evidence",
                        "Decisions based on limited or incomplete evidence", "Decisions based on evidence"]
    evidence_status = st.radio(
        "Select evidence-based decisions status:", evidence_options, key="29")

    st.subheader(questions[31])
    risks_options = ["Supply planning meetings address emergencies only",
                     "Supply planning meetings address imminent risks", "Routine monitoring and addressing of supply risks"]
    risks_status = st.radio(
        "Select supply planning risks status:", risks_options, key="30")

    st.subheader(questions[32])
    comments = st.text_area("Provide comments here:",
                            key="forecasting_supply_planning")

    responses = [
        work_plans_status, stakeholders_status, meetings_status,
        review_status, flexibility_status, decisions_status,
        evidence_status, risks_status, comments
    ]

    answers_df = pd.DataFrame(responses, columns=["answer"])
    questions_answers_df = pd.concat(
        [questions_df[24:33].reset_index(drop=True), answers_df], axis=1)
    scores = [
        work_plans_options.index(work_plans_status) + 1,
        stakeholders_options.index(stakeholders_status) + 1,
        meetings_options.index(meetings_status) + 1,
        review_options.index(review_status) + 1,
        flexibility_options.index(flexibility_status) + 1,
        decisions_options.index(decisions_status) + 1,
        evidence_options.index(evidence_status) + 1,
        risks_options.index(risks_status) + 1
    ]

    scores_df = pd.DataFrame(scores, columns=["score"])

    combined_df = pd.concat([questions_answers_df, scores_df], axis=1)

    return combined_df


def funding_adjustments_section():
    st.subheader(questions[33])
    results_communication_options = ["Results not communicated to stakeholders",
                                     "Results partially communicated to stakeholders", "Results communicated to stakeholders"]
    results_communication_status = st.radio(
        "Select communication of results status:", results_communication_options)

    st.subheader(questions[34])
    adjustments_communication_options = ["Adjustments not communicated to stakeholders",
                                         "Adjustments partially communicated to stakeholders", "Adjustments communicated to stakeholders"]
    adjustments_communication_status = st.radio(
        "Select communication of adjustments status:", adjustments_communication_options)

    st.subheader(questions[35])
    adjustments_implementation_options = [
        "Adjustments not implemented", "Adjustments partially implemented and/or untimely", "Adjustments implemented in a timely manner"]
    adjustments_implementation_status = st.radio(
        "Select adjustments implementation status:", adjustments_implementation_options)

    st.subheader(questions[36])
    total_funding_options = ["Funding not available for total commodity requirement",
                             "Limited funding available for total commodity requirement", "Funding available for total commodity requirement"]
    total_funding_status = st.radio(
        "Select total funding availability status:", total_funding_options)

    st.subheader(questions[37])
    adjustments_funding_options = ["Funding not available for recommended adjustments",
                                   "Limited funding available for recommended adjustments", "Funding available for recommended adjustments"]
    adjustments_funding_status = st.radio(
        "Select adjustments funding availability status:", adjustments_funding_options)

    st.subheader(questions[38])
    comments = st.text_area("Provide comments here:", key="funding_adjst")

    responses = [
        results_communication_status, adjustments_communication_status,
        adjustments_implementation_status, total_funding_status,
        adjustments_funding_status, comments
    ]

    answers_df = pd.DataFrame(responses, columns=["answer"])
    questions_answers_df = pd.concat(
        [questions_df[33:].reset_index(drop=True), answers_df], axis=1)
    scores = [
        results_communication_options.index(results_communication_status) + 1,
        adjustments_communication_options.index(
            adjustments_communication_status) + 1,
        adjustments_implementation_options.index(
            adjustments_implementation_status) + 1,
        total_funding_options.index(total_funding_status) + 1,
        adjustments_funding_options.index(adjustments_funding_status) + 1]

    scores_df = pd.DataFrame(scores, columns=["score"])

    combined_df = pd.concat([questions_answers_df, scores_df], axis=1)

    return combined_df


countries_main = [
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda",
    "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain",
    "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia",
    "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso",
    "Burundi", "Côte d'Ivoire", "Cabo Verde", "Cambodia", "Cameroon", "Canada",
    "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros", "Congo (Congo-Brazzaville)",
    "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czechia (Czech Republic)", "Democratic Republic of the Congo",
    "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador",
    "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini (formerly Swaziland)", "Ethiopia", "Fiji", "Finland",
    "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala",
    "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Holy See", "Honduras", "Hungary", "Iceland",
    "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan",
    "Kazakhstan", "Kenya", "Kiribati", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho",
    "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia",
    "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia",
    "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar (formerly Burma)",
    "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Korea",
    "North Macedonia (formerly Macedonia)", "Norway", "Oman", "Pakistan", "Palau", "Palestine State", "Panama",
    "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia",
    "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino",
    "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore",
    "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Korea", "South Sudan", "Spain",
    "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Tajikistan", "Tanzania", "Thailand",
    "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu",
    "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States of America", "Uruguay",
    "Uzbekistan", "Vanuatu", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"
]

countries = [
    "Nigeria", "Democratic Republic of the Congo",
    "Ethiopia", "Mozambique", "Pakistan"
]


review_periods = [
    "Q1 2024", "Q2 2024", "Q3 2024", "Q4 2024"
]

# Authenticate with Google Drive

# Authenticate with Google Drive


def authenticate():
    scope = ["https://spreadsheets.google.com/feeds",
             "https://www.googleapis.com/auth/drive"]
    # Read Google Drive credentials from environment variable
    creds_dict = {
        "type": os.environ["GOOGLE_TYPE"],
        "project_id": os.environ["GOOGLE_PROJECT_ID"],
        "private_key_id": os.environ["GOOGLE_PRIVATE_KEY_ID"],
        "private_key": os.environ["GOOGLE_PRIVATE_KEY"].replace('\\n', '\n'),
        "client_email": os.environ["GOOGLE_CLIENT_EMAIL"],
        "client_id": os.environ["GOOGLE_CLIENT_ID"],
        "auth_uri": os.environ["GOOGLE_AUTH_URI"],
        "token_uri": os.environ["GOOGLE_TOKEN_URI"],
        "auth_provider_x509_cert_url": os.environ["GOOGLE_AUTH_PROVIDER_X509_CERT_URL"],
        "client_x509_cert_url": os.environ["GOOGLE_CLIENT_X509_CERT_URL"]
    }
    creds = service_account.Credentials.from_service_account_info(
        creds_dict, scopes=scope)
    client = gspread.authorize(creds)
    return client


def append_to_sheet(df, sheet_name):
    client = authenticate()
    sheet = client.open(sheet_name).sheet1  # Change the sheet name as needed
    existing_data = sheet.get_all_records()
    existing_df = pd.DataFrame(existing_data)
    combined_df = pd.concat([existing_df, df], ignore_index=True)
    set_with_dataframe(sheet, combined_df)


if __name__ == "__main__":
    print(purpose, instructions)
