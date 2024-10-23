// we have a list we need to seperate between it's items withe the seperator that the user give 
// we create a new string to put the result inside it 
// we check if the list is not empty
// if the list is empty we return an empty string 
// if the list has only one item the result string will be the same as the item and return the result
// else 
// we add the first item to the result string
// we add a seperator to the result string before adding the next item
// we start looping from the second item and for each item we add a seperator and the item to the result string
// return the result
function join(arr, separator){
    var result = "";
    if(arr.length==0)
        return result
    else if(arr.length){
        result=arr[0]
        return result
    }
    else { 
        result=arr[0]+separator
        for(var i=1;i<arr.length;i++){
            result=result+arr[i]+separator

            
            
        }
        
        
    }






}
