excel_etpl_field_names =\
  {
    "ID",
    "TYPEID",
    "STATUSID",
    "USERID",
    "FEIN",
    "OFFICIALNAME",
    "STREET1",
    "STREET2",
    "CITY",
    "STATE",
    "ZIP",
    "PHONE",
    "FAX",
    "CONTACTFIRSTNAME",
    "CONTACTLASTNAME",
    "CONTACTTITLE",
    "MSTREET1",
    "MSTREET2",
    "MCITY",
    "MSTATE",
    "MZIP",
    "WEBSITE",
    "EMAIL",
    "COUNTY",
    "LICENSEDBY",
    "LICENSINGAGENCYID",
    "NONGOVAPPROVAL",
    "BUSROUTE1",
    "BUSROUTE2",
    "WIBCOMMENTS",
    "STATECOMMENTS",
    "AGREEMENT",
    "SUBMITTEDBYPROVIDER",
    "PHONEEXT",
    "TRAINROUTE1",
    "TRAINROUTE2",
    "DATEAPPROVALEXPIRATION",
    "ISDELETED",
    "DATEDELETED",
    "ID_1",
    "PROVIDERID",
    "STATUSID_1",
    "CIPCODE",
    "APPROVINGAGENCYID",
    "OTHERAGENCY",
    "DATEAPPROVALEXPIRATION_1",
    "SUBMITTEDTOWIB",
    "TUITION",
    "FEES",
    "BOOKSMATERIALSCOST",
    "SUPPLIESTOOLSCOST",
    "OTHERCOSTS",
    "TOTALCOST",
    "PREREQUISITES",
    "WIAELIGIBLE",
    "LEADTOLICENSE",
    "LICENSEID",
    "LEADTOINDUSTRYCREDENTIAL",
    "INDUSTRYCREDENTIALID",
    "FINANCIALAID",
    "DESCRIPTION",
    "TOTALCOURSEHOURS",
    "CREDITS",
    "TOTALCLOCKHOURS",
    "CALENDARLENGTHID",
    "FEATURESDESCRIPTION",
    "SUBMITTERNAME",
    "AGREEMENT_1",
    "CONTACTNAME",
    "CONTACTEMAIL",
    "CONTACTPHONEEXTENSION",
    "NAME_1",
    "WIBCOMMENTS_1",
    "STATECOMMENTS_1",
    "DEGREEID",
    "LEADTODEGREE",
    "UPLOADID",
    "ISDELETED_1",
    "DATEDELETED_1",
    "IMPORTID",
    "SCHOOLIDENTIFICATIONNUMBER"
    }

sql_etpl_field_names =\
  {
    "OFFICIALNAME",
    "CIPCODE",
    "APPROVINGAGENCYID",
    "OTHERAGENCY",
    "SUBMITTEDTOWIB",
    "TUITION",
    "FEES",
    "BOOKSMATERIALSCOST",
    "SUPPLIESTOOLSCOST",
    "OTHERCOSTS",
    "TOTALCOST",
    "PREREQUISITES",
    "WIAELIGIBLE",
    "LEADTODEGREE",
    "DEGREEAWARDED",
    "LEADTOLICENSE",
    "LICENSEAWARDED",
    "LEADTOINDUSTRYCREDENTIAL",
    "INDUSTRYCREDENTIAL",
    "FINANCIALAID",
    "DESCRIPTION",
    "CREDIT",
    "TOTALCLOCKHOURS",
    "CALENDARLENGTHID",
    "FEATURESDESCRIPTION",
    "WIBCOMMENT",
    "STATECOMMENT",
    "SUBMITTED",
    "APPROVED",
    "CONTACTNAME",
    "CONTACTPHONE",
    "PHONEEXTENSION",
    "PROGRAMID",
    "STATUSNAME",
    "id"
  }

labor_etpl_field_names =\
  {
    "providerid",
    "officialname",
    "cipcode",
    "approvingagencyid",
    "otheragency",
    "submittedtowib",
    "tuition",
    "fees",
    "booksmaterialscost",
    "suppliestoolscost",
    "othercosts",
    "totalcost",
    "prerequisites",
    "wiaeligible",
    "leadtodegree",
    "degreeawarded",
    "leadtolicense",
    "licenseawarded",
    "leadtoindustrycredential",
    "industrycredential",
    "financialaid",
    "description",
    "credit",
    "totalclockhours",
    "calendarlengthid",
    "featuresdescription",
    "wibcomment",
    "statecomment",
    "submitted",
    "approved",
    "contactname",
    "contactphone",
    "phoneextension",
    "programid",
    "statusname",
    "providerid",
    "name",
    "schoolidentificationnumber",
    "street1",
    "street2",
    "city",
    "state",
    "zip",
    "county",
    "mstreet1",
    "mstreet2",
    "mcity",
    "mstate",
    "mzip",
    "contactfirstname",
    "contactlastname",
    "contacttitle",
    "phone",
    "phoneextension",
    "fax",
    "website",
    "email",
    "licensingagencyid",
    "typeid",
    "nongovapproval",
    "certapprovalexp",
    "customized",
    "distancelearning",
    "speakspanish",
    "otherlanguages",
    "languages",
    "careerassist",
    "onestopcareer",
    "personalassist",
    "accessajbatb",
    "childcare",
    "assistobtainingchildcare",
    "eveningcourses",
    "accessfordisabled",
    "busroute1",
    "busroute2",
    "trnroute1",
    "trnroute2",
    "wibcomment",
    "providerstatecomment",
    "dtsubmitted",
    "statusname"
  }


# # Note: these are older mappings
# # todo: remove when an inital standardization works
# This dictionary maps fields of the same content but having different names.
sql_excel_field_map =\
  {
    "OFFICIALNAME": "NAME",
    "WIAELIGIBLE": "IS_WIOA",
    "LEADTODEGREE": "Mentioned_Associates",
    "LEADTOINDUSTRYCREDENTIAL": "Mentioned_Certificate"
  }

# This dictionary maps fields back to what sql expects, and type
excel_to_sql_name_map =\
  {
    "NAME": "OFFICIALNAME",
    "IS_WIOA": "WIAELIGIBLE",
    "Mentioned_Associates": "LEADTODEGREE",
    "Mentioned_Certificate": "LEADTOINDUSTRYCREDENTIAL"
  }

sql_type_map =\
  {
    "officialname": "string",
    "wiaeligible": "boolean",
    "leadtodegree": "boolean",
    "leadtoindustrycredential": "boolean"
  }

# Note: using the originally provide field names is confusing,
# should be updated to what labor is sending after a successful
# run
labor_fields_to_internal =\
  {
    "name": "name_1",
    "officialname": "name",
    "wiaeligible": "is_wioa",
    "leadtodegree": "mentioned_associates",
    "leadtoindustrycredential": "mentioned_certificate"
    "statecomment": "statecomments"
    "providerstatecomment": "statecomments_1"
  }

# This dictionary maps fields back to what sql expects, and type
internal_fields_to_labor =\
  {
    "name": "officialname",
    "name_1": "name",
    "is_wioa": "wiaeligible",
    "mentioned_associates": "leadtodegree",
    "mentioned_certificate": "leadtoindustrycredential"
    "statecomments": "statecomment"
    "statecomments_1": "providerstatecomment"
  }

sql_type_map =\
  {
    "officialname": "string",
    "wiaeligible": "boolean",
    "leadtodegree": "boolean",
    "leadtoindustrycredential": "boolean"
  }