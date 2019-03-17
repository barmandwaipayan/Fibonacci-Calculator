$(document).ready(function(){
  $("#fiboform").submit(function(){
    let ajaxTime= new Date().getTime(); // Click time
    event.preventDefault(); // Stop from submission
    let number = $("#number").val(); // Get the number entered
    let get_url = $("#url").text() + 'getfibo/' + number + '/'; // Fetch the url from template
    // Check if number number has been entered
    if(number != ''){
      $.ajax({
        url: get_url,
        contentType: "application/json",
        dataType: 'json',

        success: function(result){
          let num = result[0]["number"];
          let fibo = result[0]["fibo"];
          let fibo_output = "The " + num;
          // Formatting output to 1st/2nd/3rd/nth
          switch(num)
          {
            case(1): {
              fibo_output += 'st';
              break;
            }
            case(2): {
              fibo_output += 'nd';
              break;
            }
            case(3): {
              fibo_output += 'rd';
              break;
            }
            default: {
              fibo_output += 'th';
              break;
            }
          }

          fibo_output += ' Fibonacci number is ' + fibo;

          $("#fibo_output").text(fibo_output);
          let totalTime = new Date().getTime()-ajaxTime; // Result time
          $("#fibo_output").show(); // Unhide
          $("#time_req").text("Result fetched in " + totalTime + "ms");
          $("#time_req").show(); // Unhide
        }
      })
    }
    else{
      alert('Please enter a number'); // If number field is blank
    }
  })
})
