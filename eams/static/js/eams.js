// alert dismisser
setTimeout(function (){
    $('#alert').hide();
}, 3000);
$('#alert').on('click', 'button.close', function () {
    $('#alert').hide();
});

// hide messages
function hideMessage() {
    var message_el = document.getElementById("message");
    if (message_el) {
        setTimeout(function () {
            message_el.style.display = "none";
        }, 3000);
    }
}
window.onload = hideMessage;


// // get student according to their programme of study
// $(document).ready(function (){
//     // console.log('Document ready');
//     $('#programme').change(function () {
//         // console.log('Programme change event');
//         var selectedProgrammeId = $(this).val();
//         var selectedStudentId = $(this).val();
//         // var selectedCourseId = $(this).val();

//         // send ajax to retrieve data
//         $.ajax({
//             url: '/eams/student_cw/',
//             type: 'GET',
//             data: {
//                 programme_id: selectedProgrammeId,
//                 student_id: selectedStudentId,
//                 // course_id: selectedCourseId,
//                 // staff_id: {{ user_id }},
//             },
//             success: function (data) {
//                 var studentsHtml = '';  // Initialize an empty string to store HTML content
//                 // Iterate through the list of students and build HTML content
//                 for (var i = 0; i < data.students.length; i++) {
//                     studentsHtml += '<tr>';
//                     studentsHtml += '<td>' + (i + 1) + '</td>';
//                     studentsHtml += '<td>' + data.students[i].reg_number + '</td>';
//                     studentsHtml += '<td>' + data.students[i].programme_abbrevation + '</td>';
//                     var matchingCourse = data.courses.find(course => course.id === data.students[i].course_id);
//                     if (matchingCourse) {
//                         studentsHtml += '<td>' + matchingCourse.code + '</td>';
//                     } else {
//                         studentsHtml += '<td></td>'; // Handle the case when no matching course is found
//                     }
//                     studentsHtml += '<td><form action="" id="submit_student_cw_form" method="post">';
//                     studentsHtml += '{% csrf_token %}';
//                     studentsHtml += '<input type="hidden" name="programme_id" value="' + selectedProgrammeId + '">';
//                     // studentsHtml += '<input type="hidden" name="course_id" value="' + data.students[i].course_id + '">';
//                     studentsHtml += '<input type="hidden" name="student_id" value="' + data.students[i].id + '">';
//                     studentsHtml += '<div class="form-group">';
//                     studentsHtml += '<input type="number" name="course_work_value" id="cw" placeholder="Enter CW" class="cw-input form-control" required>';
//                     studentsHtml += '</div>';
//                     // studentsHtml += '<input type="hidden" name="id" class="course_id form-control" value="' + data.students[i].course_id +' ">';
//                     studentsHtml += '<div class="form-group">';
//                     studentsHtml += '<input type="submit" value="Submit CW" class="submit-button primary form-control">';
//                     studentsHtml += '</div>';
//                     studentsHtml += '</form></td>';
//                     studentsHtml += '<td><div class="row">';
//                     studentsHtml += '<div class="col-md-4"> <i class="fa fa-eye text-primary"></i> </div>';
//                     studentsHtml += '<div class="col-md-4"> <i class="fa fa-edit text-primary"></i> </div>';
//                     studentsHtml += '<div class="col-md-4"> <i class="fa fa-trash text-danger"></i> </div>';
//                     studentsHtml += '</div></td>';
//                     studentsHtml += '</tr>';
//                 }       
//                 $('#students-container').html(studentsHtml);   
//             },
//             error: function () {
//                 console.log("error")
//             }
//         });
//     });

//     // cw submitssion using ajax
//     $(document).on('click', '.submit-button', function (e) {
//         e.preventDefault();
//         // form data
//         var form = $(this).closest('form');
//         var formData = form.serialize();
//         var courseId = form.find('input[name="id"]').val();
//         $.ajax({
//             // url: '/eams/student_cw/',
//             url: form.attr('action'),
//             type: "POST",
//             // data: formData,
//             data: formData + '&id=' + courseId,
//             success: function (response){
//                 if(response.success) {
//                     var course_id_value = response.course_id;
//                     form.find(".course_id").val(course_id_value);
//                     form.find(".cw-input").prop('readonly', true);
//                     form.find(".submit-button").val("Update CW").addClass("btn btn-success disabled update-class");
//                     $('#alert').html('<div class="alert alert-success">Course Work Submitted <button type="button" class="close" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>').show();
//                 } 
//                 else {
//                     $('#alert').html('<div class="alert alert-danger">' + response.errors + '</div>').show();
//                 }
//             },
//             error: function(){
//                 $('#alert').html('<div class="alert alert-danger">Error in AJAX request ' + response.errors + '</div>').show();
//             }
//         });
//     });

//     // update cw value
//     $(document).on('click', '.update-class', function (e) {
//         e.preventDefault();
//         var form = $(this).closest('form');
//         var formData = form.serialize();

//         $.ajax({
//             url: form.attr('action'),
//             type: 'POST',
//             data: formData,
//             success: function (response) {
//                 if (response.success) {
//                     $('#alert').html('<div class="alert alert-success">Course Updated Successfully</div>').show();
//                 }
//                 else{
//                     $('#alert').html('<div class="alert alert-danger">Error in AJAX request</div>').show();
//                 }
//             },
//             error: function () {
//                 $('#alert').html('<div class="alert alert-danger">Error in AJAX request ' + response.errors + '</div>').show();
//             }
//         });
//     });

//     // update corse code to all student
//     $(document).on('click', '.submit-course-work', function(e){
//         e.preventDefault();
//         var courseCode = $('#course').val();
//         var programmeId = $('#programme').val();
//         // var student_course_work = td.find('tr[name="student_course_work"']').val();
//         $.ajax({
//             url: '/eams/student_cw/',
//             type: 'POST',
//             data: {
//                 // course_work_value: '',
//                 programmeId: programmeId,
//                 // student_id: '',
//                 // id: '',
//                 courseCode: courseCode,
//                 csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
//             },
//             success: function (response) {
//                 if (response.success) {
//                     $('#alert').html('<div class="alert alert-success">Course Code Add</div>').show();
//                 }
//                 else{
//                     $('#alert').html('<div class="alert alert-danger">Error in AJAX request</div>').show();
//                 }
//             },
//             error: function () { 
//                 alert('fail');
//                 $('#alert').html('<div class="alert alert-danger">Error in AJAX request ' + response.errors + '</div>').show();
//             }
//         })
//     });
    
// });

// setTimeout(function (){
//     $('#alert').hide();
// }, 3000);
// $('#alert').on('click', 'button.close', function () {
//     $('#alert').hide();
// });


// exam attendence
$(document).ready(function(){
    // get unit data
    $('#unit').change(function () {
        var selectUnitId = $(this).val();

        // check if unt is selected
        if (selectUnitId) {
            $('#depertment').prop('disabled', false);
            // get progrm data based on above unit
            $.ajax({
                url: '/eams/exam_attendance',
                type: 'GET',
                data: {
                    unit_id: selectUnitId
                },
                success: function (data) {
                    var depertmentSelected = $('#depertment')
                    depertmentSelected.empty();
                    // option
                    depertmentSelected.append('<option selected hidden>Choose Department</option>');
                    for (var i = 0; i < data.length; i++) {
                        depertmentSelected.append('<option value="' + data[i].id + '">' + data[i].name +'</option>');
                    }
                },
                error: function () {
                    console.log('error');
                }
            });
        }
        else{
            $('#department').prop('disabled', true).val('');
        }
    });
    
    // get all programme data which belong in above depertment
    $('#depertment').change(function () {
        var selectedDepartmentId = $(this).val();

        if (selectedDepartmentId) {
            $('#programmeOnExam').prop('disabled', false);
            $.ajax({
                url: '/eams/exam_attendance',
                type: 'GET',
                data: {
                    department_id: selectedDepartmentId
                },
                success: function (data) {
                    var programmeOnExam = $('#programmeOnExam');
                    programmeOnExam.empty();

                    programmeOnExam.append('<option selected hidden>Choose Programme</option>');
                    for (var i  = 0; i < data.length; i++) {
                        programmeOnExam.append('<option value="' + data[i].id + '">' + data[i].name +'</option>')                        
                    }
                },
                error: function () {
                    console.log('error');
                }
            });
        }
        else{
            $('#programmeOnExam').prop('disabled', true).val('');
        }
    });

    // get all course data which belong in above semester
    $('#semester').change(function () {
        var selectedSemesterId = $(this).val();

        if (selectedSemesterId) {
            $('#course').prop('disabled', false);            
            $.ajax({
                url: '/eams/exam_attendance',
                type: 'GET',
                data: {
                    semester_id: selectedSemesterId
                },
                success: function (data) {
                    var course = $('#course');
                    course.empty();

                    course.append('<option selected hidden>Choose Course</option>');
                    for (var i = 0; i < data.length; i++) {
                        course.append('<option value="' + data[i].id +'">' + data[i].name +'</option>')                        
                    }
                },
                error: function(){
                    console.log('error');
                }
            });
        }
        else{
            $('#course').prop('disabled', true).val('');
        }
    });

    // choose exam type and submit exam attendence record
    $('#exam_attendence_step1').on('submit', function (e) {
        e.preventDefault();
        $.ajax({
            url: '/eams/exam_attendance',
            type: "POST",
            data: $(this).serialize(),
            success: function (response) {
                document.getElementById("exam_attendence_step1").reset();
                if (response.success) {
                    $('#alert').html('<div class="alert alert-success">Data Submitted Succssfully!</div>').show();
                }
                else{
                    $('#alert').html('<div class="alert alert-error">Error In Data Submission Try Again</div>').show();
                }
            },
            error: function (error) { 
                $('#alert').html('<div class="alert alert-danger">Error in AJAX request ' + response.errors + '</div>').show();
            }
        });
        return false;
    });

    // update ex-status make and end
    $('#update_exam_end_status').on('submit', function (e) {
        e.preventDefault();
        const response = confirm("Are you sure you want to end This Exam?");
        if (response) {
            $.ajax({
                url: '/eams/exam_attendance',
                type: 'POST',
                data: $(this).serialize(),
                success: function (response) {
                    document.getElementById("update_exam_end_status").reset();
                    if (response.success) {
                        $('#alert').html('<div class="alert alert-success">Exam End Successfully</div>').show();
                    }
                    else{
                        $('#alert').html('<div class="alert alert-error">Error In Data Submission Try Again</div>').show();
                    } 
                },
                error: function (error) {
                    $('#alert').html('<div class="alert alert-danger">Error in AJAX request ' + response.errors + '</div>').show();
                }
            });
            return false;
        }
    });

    // Function to get CSRF token from the cookie
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Check if the cookie name matches the desired token name
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }  


    // student_attendance_history
    $('#get_programme_to_student').change(function (e) {
        e.preventDefault();
        var programme_to_student = $(this).val();
        $.ajax({
            url: '/eams/exam_attendance',
            type: 'GET',
            data: {get_programme_to_student: programme_to_student},
            success: function (data) {
                $('#student_history_data').empty();
                console.log(data);
                if (data.length > 0) {
                    for (var i = 0; i < data.length; i++) {
                        $('#student_history_data').append(
                            '<tr>' +
                            '<td>' + data[i].booklet_number + '</td>' +
                            '<td>' + data[i].signin_flag + '</td>' +
                            '<td>' + data[i].signout_flag + '</td>' +
                            '<td>' + data[i].biometric_data + '</td>' +
                            '<td>' + data[i].exam_attendace + '</td>' +
                            '</tr>'
                        );
                    }
                }
                else {
                    $('#student_history_data').append(
                        '<tr><td colspan="10">No data available</td></tr>'
                    );
                }
            },
            error: function () {
                $('#student_history_data').empty();
                $('#student_history_data').append(
                    '<tr><td colspan="10">Error fetching data</td></tr>'
                );
            }
        });
    });

    // update_student_who_attend_exam submt
    // $('#update_student_who_attend_exam').on('submit', function (e) {
    //     e.preventDefault();
    //     // var form =   $(this).serialize();
    //     $.ajax({
    //         url: "/eams/exam_attendance",
    //         type: "GET",
    //         data: { 
    //             reg_number: $('#reg_number').val(),
    //             // csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
    //         },
    //         // headers: {'X-CSRFToken': csrftoken},  // Include CSRF token in headers
    //         success: function (data) {
    //             if (data.reg_number_exists && data.fingerprint_match) {
    //                 $('#alert').html('<p class="alert alert-success">submited successfully</p>').show();
    //                 // Proceed with form submission
    //                 // $.ajax({
    //                 //     url: "/eams/exam_attendance",
    //                 //     type: "POST",
    //                 //     data: $('#update_student_who_attend_exam').serialize(),
    //                 //     success: function (data) {
    //                 //         // Handle the response from the server after form submission
    //                 //         console.log("data");
    //                 //     },
    //                 //     error: function (insertDataError) {
    //                 //         console.log('Error submitting form data:', insertDataError);
    //                 //         // Handle error if needed
    //                 //     }
    //                 // });  
    //                 $('#update_student_who_attend_exam').off('submit').submit();
            
    //             } 
    //             else {
    //                 var confirmSubmission = confirm('Registration number does not match or fingerprint does not match. Do you still want to submit the form?');
    //                 // If user confirms, proceed with form submission
    //                 if (confirmSubmission) {
    //                     $('#update_student_who_attend_exam').submit();
    //                 } 
    //             }
    //         },
    //         error: function (error){
    //             console.log('Error in ajax');
    //         }
    //     });
    //     return false;
    // });

    // update_student_info
    $('#update_student_info').on('submit', function (e) {
        e.preventDefault();
        var csrftoken = getCookie('csrftoken');
        formData = $(this).serialize();
        $.ajax({
            url:  $('#update_student_info').attr("data-url"),
            type: "POST",
            data: formData,
            headers: {'X-CSRFToken': csrftoken},  // Include CSRF token in headers
            success: function (data) {
                $('#alert').html('<p class="alert alert-success">Information Updated Successfully</p>').show()
            }, 
            error: function (error) {
                console.log('Ajax Error');
            }
        });
        return false;
    });
    
    // student_finger_info
    $('#student_finger_info').on('submit', function (e) {
        e.preventDefault();
        formData = $(this).serialize();
        $.ajax({
            url: $('#student_finger_info').attr('data-url'),
            type: "POST",
            data: formData, 
            success: function (data) {
                $('#alert').html('<p class="alert alert-success">Fingerprint Registered</p>').show();
            },
            error: function (error) {
                console.log('error in ajax');
            }
        });
    });

    
    // selected student to attende exam based on their programme
    $(document).ready(function() {
        $('#programme_id_on_exam').change(function() {
            var programmeId = $(this).val(); // Get the selected programme ID
            $.ajax({
                url: 'http://127.0.0.1:8000/eams/exam_attendance_step_two/', // Update the URL to include the full path
                method: 'GET',
                data: {
                    programme_id: programmeId
                },
                success: function(response) {
                    $('#search_input').prop('disabled', false); // Enable search input field
                    console.log(response);
                    // Clear previous data
                    $('.list_of_student.sign_in').empty();
                    $('.list_of_student.sign_out').empty();
                    // Populate the list of students for sign in
                    var signInList = '';
                    response.forEach(function(regNumber) {
                        signInList += '<div class="card">';
                        signInList += '<div class="card-header">';
                        signInList += '<p class="text-center">' + regNumber + '</p>';
                        signInList += '</div>';
                        signInList += '<div class="card-body">';
                        signInList += '<form action="{% url "submit_signout_student" %}" method="post">';
                        signInList += '{% csrf_token %}';
                        signInList += '<div class="form-group">';
                        signInList += '<label for="fingerprint">Click To Attach Fingerprint</label>';
                        signInList += '<input type="text" name="biometric_data" id="biometric_data_id" placeholder="Enter biometric_data_id" class="form-control" value="1">';
                        signInList += '<input type="text" name="reg_number" id="reg_number" placeholder="Enter reg_number" class="form-control" value="' + regNumber + '">';
                        signInList += '</div>';
                        signInList += '<input type="submit" class="form-control primary" value="Submit">';
                        signInList += '</form>';
                        signInList += '</div>';
                        signInList += '</div>';
                        signInList += '<br>';
                    });
                    $('.list_of_student.sign_in').html(signInList);
    
                    // Populate the list of students for sign out
                    var signOutList = '';
                    response.forEach(function(regNumber) {
                        signOutList += '<div class="card">';
                        signOutList += '<div class="card-header">';
                        signOutList += '<p class="text-center">' + regNumber + '</p>';
                        signOutList += '</div>';
                        signOutList += '<div class="card-body">';
                        signOutList += '<form action="{% url "submit_signout_student" %}" method="post">';
                        signOutList += '{% csrf_token %}';
                        signOutList += '<div class="form-group">';
                        signOutList += '<label for="fingerprint">Click To Attach Fingerprint</label>';
                        signOutList += '<input type="text" name="biometric_data" id="biometric_data_id" placeholder="Enter biometric_data_id" class="form-control" value="1">';
                        signOutList += '<input type="text" name="reg_number" id="reg_number" placeholder="Enter reg_number" class="form-control" value="' + regNumber + '">';
                        signOutList += '</div>';
                        signOutList += '<input type="submit" class="form-control primary" value="Submit">';
                        signOutList += '</form>';
                        signOutList += '</div>';
                        signOutList += '</div>';
                        signOutList += '<br>';
                    });
                    $('.list_of_student.sign_out').html(signOutList);
                },
                error: function(xhr, status, error) {
                    console.error('Error:', error);
                }
            });
        });
    });
    


    $('#sign_in_form').on('submit', function(e) {
        e.preventDefault();
        var formData = $(this).serialize();
        submitForm(formData,  '{% url "submit_signin_student" %}');
    });

    $('#sign_out_form').on('submit', function(e) {
        e.preventDefault();
        var formData = $(this).serialize();
        submitForm(formData, '/exam/submit_signout_student', 'Sign Out');
    });

    function submitForm(formData, url, action) {
        $.ajax({
            url: url,
            type: "POST",
            data: formData,
            success: function(data) {
                $('#alert').html('<p class="alert alert-success">' + action + ' Successful</p>').show();
            },
            error: function(xhr, status, error) {
                var response = JSON.parse(xhr.responseText);
                $('#alert').html('<p class="alert alert-danger">' + response.errors + '</p>').show();
            }
        });
    }
});



// exam attendance step one and two
function openExam(evt, examAction) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(examAction).style.display = "block";
    evt.currentTarget.className += " active";
}

// Student_Biometric
function openStudentBiometric(evt, biometricAction) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(biometricAction).style.display = "block";
    evt.currentTarget.className += " active";
}