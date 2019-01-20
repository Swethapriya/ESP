
document.getElementById("app").addEventListener("click",function(){
    document.getElementsByClassName("_39LWd")[0].innerHTML = "esp text suggest";
});

var message = "";
var bigrams = {};

document.getElementById("app").addEventListener("keyup", function(e){
    //logging message
if(e.keyCode!=13){
  message = document.getElementsByClassName("_2S1VP copyable-text selectable-text")[0].innerHTML;
  if(message.indexOf("<div") >= 0){
      message = message.substring(0,message.indexOf("<div"));
  }
}
console.log(message);
    //handling space
if(e.keyCode == 32){
  var words = message.split(" ");
	current_word =  words[words.length-2];
  if(bigrams.hasOwnProperty(current_word)){
    contending_words = bigrams[current_word];
   	console.log(contending_words);
   	keysSorted = Object.keys(contending_words).sort(function(a,b){return contending_words[a]-contending_words[b]});
   	esp_text_suggest = keysSorted[keysSorted.length-1];
   	var element = document.getElementsByClassName("_2S1VP copyable-text selectable-text")[0];
    var div = document.getElementsByClassName("_3F6QL _2WovP")[0];
    element.innerHTML = message + "<div contentEditable='true' data-placeholder='Enter text here'></div>"
    //element.innerHTML = message + "<div style = 'display: inline-block; pointer-events: none !important; color: #a4a4a4 !important; user-select: none !important;-moz-user-select: none !important;-khtml-user-select: none !important;-webkit-user-select: none !important;-o-user-select: none !important;'>" + esp_text_suggest +"</div>";
   	//element.innerHTML = message + "<div style='display:  inline-block; pointer-events: none; color: #a4a4a4 !important; user-select: none !important;-moz-user-select: none !important;-khtml-user-select: none !important;-webkit-user-select: none !important;-o-user-select: none !important;'>" + esp_text_suggest + "</div>";
  }
}

//handling enter
else if(e.keyCode == 13){
    	words = message.split(" ");
      words = words.filter(function (el) {
        return el != "";
      });
    	for(i=0;i<words.length-1;i++){
    		first_word = words[i];
    		second_word = words[i+1];
    		if(bigrams.hasOwnProperty(first_word)){
    			if(bigrams[first_word].hasOwnProperty(second_word)){
    				bigrams[first_word][second_word] += 1;
    			}
    			else{
    				bigrams[first_word][second_word] = 1
    			}

    		}
    		else{
    			bigrams[first_word] = {};
    			bigrams[first_word][second_word] = 1;
    		}
    		console.log(first_word)
    	}
    }
});
