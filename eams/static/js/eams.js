// function hideMessage() {
//     var message_el = document.getElementById("message");
//     if (message_el) {
//         setTimeout(function () {
//             message_el.style.display = "none";
//         }, 3000);
//     }
// }
// window.onload = hideMessage;            

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
    $('#exam-attendence').on('submit', function (e) {
        e.preventDefault();
        $.ajax({
            url: '{url "exam_attendece"}',
            type: "POST",
            data: $this.serialize(),
            success: function (response) {
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
        })
    })
});


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