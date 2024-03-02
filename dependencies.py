import streamlit as st

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


def fsp_policies_section():
    st.subheader("Multidisciplinary Team")
    team_options = ["Absence of team",
                    "Responsibility of few individuals", "Multidisciplinary team exists"]
    team_status = st.radio("Select team status:", team_options, key="1")

    st.subheader("Inclusion of Stakeholders")
    stakeholders_options = ["Relevant stakeholders not included",
                            "Limited inclusion of stakeholders", "All relevant stakeholders included"]
    stakeholders_status = st.radio(
        "Select stakeholders inclusion status:", stakeholders_options, key="2")

    st.subheader("Work Plans, MoUs, or TORs")
    plans_options = ["Absence of ToR, MoU, or work plans", "ToR, MoU, or work plans exist but have gaps",
                     "Vaccine forecasting and supply planning prioritized"]
    plans_status = st.radio("Select work plans status:",
                            plans_options, key="3")

    st.subheader("TOR Covers Key FSP Functions")
    tor_options = ["TORs does not cover key functions",
                   "TORs cover at least two functions", "TORs cover at least four functions"]
    tor_status = st.radio("Select TORs status:", tor_options, key="4")

    st.subheader("Supply Chain Strategy")
    strategy_options = ["No SC strategy", "SC strategy but doesn't cover key technical areas",
                        "SC strategy covers key technical areas"]
    strategy_status = st.radio(
        "Select SC strategy status:", strategy_options, key="5")

    st.subheader("Commitment from Stakeholders")
    commitment_options = ["No commitment from stakeholders",
                          "Limited commitment of stakeholders", "Adequate commitment from stakeholders"]
    commitment_status = st.radio(
        "Select commitment status:", commitment_options, key="6")

    st.subheader("Resources Allocated")
    resources_options = ["Resources lacking for all FSP tasks",
                         "Resources limited for FSP tasks", "Adequate resources available for FSP tasks"]
    resources_status = st.radio(
        "Select resources status:", resources_options, key="7")
    st.subheader("Comments")
    st.text_area("Provide comments here:", key="fsp")

    return [team_options.index(team_status) + 1, stakeholders_options.index(stakeholders_status) + 1,
            plans_options.index(plans_status) +
            1, tor_options.index(tor_status) + 1,
            strategy_options.index(
                strategy_status) + 1, commitment_options.index(commitment_status) + 1,
            resources_options.index(resources_status) + 1]


def data_section():
    st.subheader(
        "Presence of a Reliable System for Collecting Disaggregated Data")
    disaggregated_options = ["The country lacks a reliable system",
                             "The system has some gaps", "The country has a reliable system"]
    disaggregated_status = st.radio(
        "Select disaggregated data status:", disaggregated_options, key="8")

    st.subheader("Access to Relevant, Quality, and Disaggregated Data")
    access_options = ["Disaggregated data is not available",
                      "Limited access to disaggregated data", "Seamless flow in accessing disaggregated data"]
    access_status = st.radio(
        "Select data access status:", access_options, key="9")

    st.subheader("Accuracy of Stock Balances")
    stock_options = ["Significant data discrepancy",
                     "Partially accurate data", "Data matches reality/is close to accurate"]
    stock_status = st.radio(
        "Select stock balances status:", stock_options, key="10")

    st.subheader("Data Reporting Practices (Timeliness of Reporting)")
    reporting_options = ["Poor data reporting practices",
                         "Ad-hoc reporting and late updating", "Data is routinely and continuously updated"]
    reporting_status = st.radio(
        "Select reporting practices status:", reporting_options, key="11")

    st.subheader("Standardized Tools for Forecasting and Supply Planning")
    tools_options = ["Tools exist but not used", "Only one tool used",
                     "Both forecasting and supply planning tools used"]
    tools_status = st.radio("Select tools status:", tools_options, key="12")

    st.subheader("Comments")
    comments = st.text_area("Provide comments here:", key="data")

    return [disaggregated_options.index(disaggregated_status) + 1,
            access_options.index(access_status) + 1,
            stock_options.index(stock_status) + 1,
            reporting_options.index(reporting_status) + 1,
            tools_options.index(tools_status) + 1]


def analysis_section():
    st.subheader("Routinely Assess Stock Status")
    stock_status_options = ["Stock status not assessed",
                            "Untimely assessment of stock status", "Routinely assessed stock status"]
    stock_status = st.radio(
        "Select stock status assessment:", stock_status_options, key="13")

    st.subheader("Methodology Used for Forecasting Vaccines")
    forecasting_method_options = [
        "Demographic/wastage factor-based", "Consumption-based", "Vaccination session-based"]
    forecasting_method = st.radio(
        "Select forecasting methodology:", forecasting_method_options, key="14")

    st.subheader("Use of Decentralized Data for National Forecasts")
    decentralized_data_options = ["Decentralized data not used for national forecasts",
                                  "Partial use of decentralized data", "Data from all levels used for national forecasts"]
    decentralized_data = st.radio(
        "Select use of decentralized data:", decentralized_data_options, key="15")

    st.subheader("Triangulation of Data from Different Sources")
    triangulation_options = ["Data from one source used",
                             "Data from limited sources used", "Data from all relevant sources used"]
    triangulation = st.radio(
        "Select data triangulation status:", triangulation_options, key="16")

    st.subheader("Calculate and Update Forecasts Based on Data")
    update_forecasts_options = ["Forecasts not calculated or updated",
                                "Forecasts available but not updated with current data", "Accurate forecasts updated based on current data"]
    update_forecasts = st.radio(
        "Select update forecasts status:", update_forecasts_options, key="17")

    st.subheader("Determine Orders in Forecast and Supply Plan")
    determine_orders_options = ["Unable to determine accurate orders",
                                "Some accuracy in determining orders", "Accurate determination of orders"]
    determine_orders = st.radio(
        "Select determine orders status:", determine_orders_options, key="18")

    st.subheader("Coverage of Forecast and Supply Plan Reports")
    plan_coverage_options = ["Reports cover 0-2 key components",
                             "Reports cover at least 3 key components", "Reports cover all 5 key components"]
    plan_coverage = st.radio(
        "Select plan coverage status:", plan_coverage_options, key="20")

    st.subheader("Conduct Scenario Monitoring")
    scenario_monitoring_options = ["Scenario monitoring not conducted",
                                   "Poorly conducted scenario monitoring", "Well-conducted scenario monitoring"]
    scenario_monitoring = st.radio(
        "Select scenario monitoring status:", scenario_monitoring_options, key="21")

    st.subheader("Ability to Estimate Vaccine Expiry")
    expiry_estimation_options = ["Inability to estimate vaccine expiry",
                                 "Limited ability to estimate expiry", "Ability to estimate expiry"]
    expiry_estimation = st.radio(
        "Select expiry estimation status:", expiry_estimation_options, key="22")

    st.subheader("Comments")
    comments = st.text_area("Provide comments here:")

    return [stock_status_options.index(stock_status) + 1,
            forecasting_method_options.index(forecasting_method) + 1,
            decentralized_data_options.index(decentralized_data) + 1,
            triangulation_options.index(triangulation) + 1,
            update_forecasts_options.index(update_forecasts) + 1,
            determine_orders_options.index(determine_orders) + 1,
            plan_coverage_options.index(plan_coverage) + 1,
            scenario_monitoring_options.index(scenario_monitoring) + 1,
            expiry_estimation_options.index(expiry_estimation) + 1]


def forecasting_supply_planning_section():
    st.subheader("Inclusion in EPI Work Plans")
    work_plans_options = ["Forecasting and supply planning activities not included",
                          "Partially included in EPI work plans", "Adequately included in EPI work plans"]
    work_plans_status = st.radio(
        "Select inclusion in EPI work plans status:", work_plans_options, key="23")

    st.subheader("Inclusion of Relevant Stakeholders")
    stakeholders_options = ["Key stakeholders not included",
                            "Limited participation by relevant stakeholders", "All relevant stakeholders included"]
    stakeholders_status = st.radio(
        "Select stakeholders inclusion status:", stakeholders_options, key="24")

    st.subheader("Regular Supply Planning Meetings")
    meetings_options = ["Meetings not being held",
                        "Irregular/ad-hoc meetings", "Regularly scheduled meetings"]
    meetings_status = st.radio(
        "Select supply planning meetings status:", meetings_options, key="25")

    st.subheader("Review of Previous Actions and Recommendations")
    review_options = ["Meetings do not review past actions and recommendations",
                      "Partial review/addressing of past actions and recommendations", "Full review and addressing of past actions and recommendations"]
    review_status = st.radio("Select review status:", review_options, key="26")

    st.subheader("Flexibility for Ad-hoc Meetings")
    flexibility_options = ["Lack of flexibility to convene ad hoc meetings",
                           "Limited flexibility to convene ad-hoc meetings", "Flexible to convene ad-hoc meetings"]
    flexibility_status = st.radio(
        "Select flexibility status:", flexibility_options, key="27")

    st.subheader("Timely and Well-coordinated Decisions")
    decisions_options = ["Decisions not made",
                         "Decisions made in an untimely manner", "Decisions made in a timely manner"]
    decisions_status = st.radio(
        "Select decisions status:", decisions_options, key="28")

    st.subheader("Evidence-based Decisions")
    evidence_options = ["Decisions not informed by evidence",
                        "Decisions based on limited or incomplete evidence", "Decisions based on evidence"]
    evidence_status = st.radio(
        "Select evidence-based decisions status:", evidence_options, key="29")

    st.subheader("Supply Planning Risks Addressed")
    risks_options = ["Supply planning meetings address emergencies only",
                     "Supply planning meetings address imminent risks", "Routine monitoring and addressing of supply risks"]
    risks_status = st.radio(
        "Select supply planning risks status:", risks_options, key="30")

    st.subheader("Comments")
    comments = st.text_area("Provide comments here:",
                            key="forecasting_supply_planning")

    return [work_plans_options.index(work_plans_status) + 1,
            stakeholders_options.index(stakeholders_status) + 1,
            meetings_options.index(meetings_status) + 1,
            review_options.index(review_status) + 1,
            flexibility_options.index(flexibility_status) + 1,
            decisions_options.index(decisions_status) + 1,
            evidence_options.index(evidence_status) + 1,
            risks_options.index(risks_status) + 1]


def funding_adjustments_section():
    st.subheader("Communication of Results to Stakeholders")
    results_communication_options = ["Results not communicated to stakeholders",
                                     "Results partially communicated to stakeholders", "Results communicated to stakeholders"]
    results_communication_status = st.radio(
        "Select communication of results status:", results_communication_options)

    st.subheader("Communication of Recommended Adjustments")
    adjustments_communication_options = ["Adjustments not communicated to stakeholders",
                                         "Adjustments partially communicated to stakeholders", "Adjustments communicated to stakeholders"]
    adjustments_communication_status = st.radio(
        "Select communication of adjustments status:", adjustments_communication_options)

    st.subheader("Timely Implementation of Recommended Adjustments")
    adjustments_implementation_options = [
        "Adjustments not implemented", "Adjustments partially implemented and/or untimely", "Adjustments implemented in a timely manner"]
    adjustments_implementation_status = st.radio(
        "Select adjustments implementation status:", adjustments_implementation_options)

    st.subheader("Availability of Funding for Total Commodity Requirement")
    total_funding_options = ["Funding not available for total commodity requirement",
                             "Limited funding available for total commodity requirement", "Funding available for total commodity requirement"]
    total_funding_status = st.radio(
        "Select total funding availability status:", total_funding_options)

    st.subheader("Availability of Funding for Recommended Adjustments")
    adjustments_funding_options = ["Funding not available for recommended adjustments",
                                   "Limited funding available for recommended adjustments", "Funding available for recommended adjustments"]
    adjustments_funding_status = st.radio(
        "Select adjustments funding availability status:", adjustments_funding_options)

    st.subheader("Comments")
    comments = st.text_area("Provide comments here:", key="funding_adjst")

    return [results_communication_options.index(results_communication_status) + 1,
            adjustments_communication_options.index(
                adjustments_communication_status) + 1,
            adjustments_implementation_options.index(
                adjustments_implementation_status) + 1,
            total_funding_options.index(total_funding_status) + 1,
            adjustments_funding_options.index(adjustments_funding_status) + 1]


if __name__ == "__main__":
    print(purpose, instructions)
