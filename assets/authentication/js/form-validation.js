(function ($) {
    "use strict";
    // Validation for order form
           $(".add-user").validate(
           {					
               rules:
               {	
                 
                   first_name:
                   {
                       required: true
                   },
                   last_name:
                   {
                       required: true
                   },
                   username:
                   {
                       required: true
                   },
                   school_name:
                   {
                       required: true
                   },
                   email:
                   {
                       required: true
                   },
                   school_code:
                   {
                       required: true
                   },
                   password:
                   {
                       required: true
                   },
                   re_password:
                   {
                       required: true
                   },
               },
               messages:
               {	
                   
                   first_name:
                   {
                       required: 'Please enter First Name'
                   },
                   last_name:
                   {
                       required: 'Please enter Father Name'
                   },
                   email:
                   {
                       required: 'Please enter CNIC#'
                   },
                   username:
                   {
                       required: 'Please enter Contact'
                   },
                   school_name:
                   {
                       required: 'Please enter name'
                   },
                   school_code:
                   {
                       required: 'Please select Date of Admission'
                   },
                   password:
                   {
                       required: 'Please select Class'
                   },
                   re_password:
                   {
                       required: 'Please select Section'
                   },
                   
               },					
               
               errorPlacement: function(error, element)
               {
                   error.insertAfter(element.parent());
               }
           });
        })(jQuery); 