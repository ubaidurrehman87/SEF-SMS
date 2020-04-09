(function ($) {
 "use strict";
 // Validation for order form
		$(".add-professors").validate(
		{					
			rules:
			{	
				gr:
				{
					required: true
				},
				name:
				{
					required: true
				},
				f_Name:
				{
					required: true
				},
				cnic:
				{
					required: true
				},
				contact1:
				{
					required: true
				},
				last_school:
				{
					required: true
				},
				admit_date:
				{
					required: true
				},
				current_class:
				{
					required: true
				},
				admit_class:
				{
					required: true
				},
				section:
				{
					required: true
				},
				status:
				{
					required: true
				},
				admit_date:
				{
					required: true
				},
				dob:
				{
					required: true
				},
				education_level:
				{
					required: true
				},
				subject:
				{
					required: true
				},
				experience:
				{
					required: true
				},
				
				shift:
				{
					required: true
				},
				gender:
				{
					required: true
				},
				religion:
				{
					required: true
				},
				
				address:
				{
					required: true
				},
				department:
				{
					required: true
				},
				
				imageico:
				{
					required: true
				}
				joining_date:
				{
					required: true
				}
				bank_name:
				{
					required: true
				}
				branch_code:
				{
					required: true
				}
				account_number:
				{
					required: true
				}
				
			},
			messages:
			{	
				gr:
				{
					required: 'Please enter Gr#'
				},
				name:
				{
					required: 'Please enter Name'
				},
				f_Name:
				{
					required: 'Please enter Father Name'
				},
				cnic:
				{
					required: 'Please enter CNIC#'
				},
				contact1:
				{
					required: 'Please enter Contact'
				},
				last_school:
				{
					required: 'Please enter name'
				},
				shif:
				{
					required: 'Please Select shift'
				},
				admit_date:
				{
					required: 'Please select Date of Admission'
				},
				current_class:
				{
					required: 'Please select Current Class'
				},
				admit_class:
				{
					required: 'Please select Admission Class'
				},
				section:
				{
					required: 'Please select Section'
				},
				status:
				{
					required: 'Please select Status'
				},
				experience:
				{
					required: 'Please select Experience'
				},
				education_level:
				{
					required: 'Please select Education Level'
				},
				subject:
				{
					required: 'Please select Subject'
				},
				religion:
				{
					required: 'Please select Religion'
				},
				gender:
				{
					required: 'Please select Gender'
				},
				dob:
				{
					required: 'Please enter Date of Birth'
				},
				
				
				address:
				{
					required: 'Please enter your address'
				},
				department:
				{
					required: 'Please enter department'
				},
				joining_date:
				{
					required: 'Please enter department'
				},
				bank_name:
				{
					required: 'Please enter Bank name'
				},
				branch_code:
				{
					required: 'Please enter Branch Code'
				},
				account_number:
				{
					required: 'Please enter Account Number'
				},
				
				imageico:
				{
					required: 'Please upload image'
				}
				
			},					
			
			errorPlacement: function(error, element)
			{
				error.insertAfter(element.parent());
			}
		});
		
 
 // Validation for order form
		$("#acount-infor").validate(
		{					
			rules:
			{	
				email:
				{
					required: true,
					email: true
				},
				phoneno:
				{
					required: true
				},
				password:
				{
					required: true,
					minlength: 3,
					maxlength: 20
				},
				confarmpassword:
				{
					required: true,
					minlength: 3,
					maxlength: 20
				}
			},
			messages:
			{	
			
				email:
				{
					required: 'Please enter your email address',
					email: 'Please enter a VALID email address'
				},
				phoneno:
				{
					required: 'Please enter mobile number'
				},
				password:
				{
					required: 'Please enter your password'
				},
				confarmpassword:
				{
					required: 'Please enter your confarm password'
				}
				
			},					
			
			errorPlacement: function(error, element)
			{
				error.insertAfter(element.parent());
			}
		});
 
 // Validation for order form
		$(".addcourse").validate(
		{					
			rules:
			{	
				coursename:
				{
					required: true
				},
				finish:
				{
					required: true
				},
				duration:
				{
					required: true
				},
				price:
				{
					required: true
				},
				imageico:
				{
					required: true
				},
				department:
				{
					required: true
				},
				description:
				{
					required: true
				},
				crprofessor:
				{
					required: true
				},
				year:
				{
					required: true
				},
				email:
				{
					required: true,
					email: true
				},
				phoneno:
				{
					required: true
				},
				password:
				{
					required: true,
					minlength: 3,
					maxlength: 20
				},
				confarmpassword:
				{
					required: true,
					minlength: 3,
					maxlength: 20
				}
			},
			messages:
			{	
				coursename:
				{
					required: 'Please enter course name'
				},
				finish:
				{
					required: 'Please select date of birth'
				},
				duration:
				{
					required: 'Please enter duration'
				},
				price:
				{
					required: 'Please enter price'
				},
				imageico:
				{
					required: 'Please enter image'
				},
				department:
				{
					required: 'Please enter department'
				},
				description:
				{
					required: 'Please enter description'
				},
				crprofessor:
				{
					required: 'Please enter course professor'
				},
				year:
				{
					required: 'Please enter year'
				},
				email:
				{
					required: 'Please enter your email address',
					email: 'Please enter a VALID email address'
				},
				phoneno:
				{
					required: 'Please enter mobile number'
				},
				password:
				{
					required: 'Please enter your password'
				},
				confarmpassword:
				{
					required: 'Please enter your confarm password'
				}
				
			},					
			
			errorPlacement: function(error, element)
			{
				error.insertAfter(element.parent());
			}
		});
		
		
		
		
 
	// Validation for login form
		$("#comment").validate(
		{					
			rules:
			{	
				name:
				{
					required: true
				},
				message:
				{
					required: true
				},
				email:
				{
					required: true,
					email: true
				}
			},
			messages:
			{	
				name:
				{
					required: 'Please enter your name'
				},
				message:
				{
					required: 'Please enter your message'
				},
				email:
				{
					required: 'Please enter your email address',
					email: 'Please enter a VALID email address'
				}
			},					
			
			errorPlacement: function(error, element)
			{
				error.insertAfter(element.parent());
			}
		});
		
		
	// Validation for login form
		$(".addlibrary").validate(
		{					
			rules:
			{	
				nameasset:
				{
					required: true
				},
				subject:
				{
					required: true
				},
				imageico:
				{
					required: true
				},
				type:
				{
					required: true
				},
				price:
				{
					required: true
				},
				year:
				{
					required: true
				},
				status:
				{
					required: true
				},
				department:
				{
					required: true
				},
				email:
				{
					required: true,
					email: true
				}
			},
			messages:
			{	
				nameasset:
				{
					required: 'Please enter your name of assets'
				},
				subject:
				{
					required: 'Please enter your subject'
				},
				imageico:
				{
					required: 'Please enter image'
				},
				department:
				{
					required: 'Please enter your department'
				},
				type:
				{
					required: 'Please enter library type'
				},
				price:
				{
					required: 'Please enter price'
				},
				year:
				{
					required: 'Please enter year'
				},
				status:
				{
					required: 'Please enter status'
				},
				email:
				{
					required: 'Please enter your email address',
					email: 'Please enter a VALID email address'
				}
			},					
			
			errorPlacement: function(error, element)
			{
				error.insertAfter(element.parent());
			}
		});
		
	// Validation for login form
		$(".add-department").validate(
		{					
			rules:
			{	
				name:
				{
					required: true
				},
				headofdepartment:
				{
					required: true
				},
				email:
				{
					required: true
				},
				phone:
				{
					required: true
				},
				noofstudent:
				{
					required: true
				},
				status:
				{
					required: true
				}
			},
			messages:
			{	
				name:
				{
					required: 'Please enter your name'
				},
				headofdepartment:
				{
					required: 'Please enter head of department'
				},
				email:
				{
					required: 'Please enter email'
				},
				phone:
				{
					required: 'Please enter your phone'
				},
				noofstudent:
				{
					required: 'Please enter no of student'
				},
				status:
				{
					required: 'Please enter status'
				}
			},					
			
			errorPlacement: function(error, element)
			{
				error.insertAfter(element.parent());
			}
		});
		
	// Validation for login form
		$("#send-mail").validate(
		{					
			rules:
			{	
				name:
				{
					required: true
				},
				headofdepartment:
				{
					required: true
				},
				email:
				{
					required: true,
					email: true
				},
				phone:
				{
					required: true
				},
				noofstudent:
				{
					required: true
				},
				status:
				{
					required: true
				}
			},
			messages:
			{	
				name:
				{
					required: 'Please enter your name'
				},
				headofdepartment:
				{
					required: 'Please enter head of department'
				},
				email:
				{
					required: 'Please enter email'
				},
				email:
				{
					required: 'Please enter your email address',
					email: 'Please enter a VALID email address'
				},
				noofstudent:
				{
					required: 'Please enter no of student'
				},
				status:
				{
					required: 'Please enter status'
				}
			},					
			
			errorPlacement: function(error, element)
			{
				error.insertAfter(element.parent());
			}
		});
		
 
})(jQuery); 