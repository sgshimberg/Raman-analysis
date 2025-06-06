
const byte numChars = 32;
char receivedChars[numChars];
char tempChars[numChars];  


int integerFromPC = 0;
float floatFromPC = 0.0;

const int RelayPin = 8;
float actual_temp, set_temp =0.0; 
float ramp_set = 0.0;
bool start_relay_Flag = false;
int ramp_counter = 0;

bool new_data = false;




void setup() {
  Serial.begin(9600);
  pinMode(RelayPin, OUTPUT);
  digitalWrite(RelayPin, LOW);

}

void loop() {

  //showParsedData();

 
//  // Setting the relay based on current temp, ramp, set temp 
 if(start_relay_Flag){
    
    //debug 
    Serial.print("relay flag ON");
    Serial.print("Current temp ");
    Serial.print(actual_temp);
    Serial.print("Set temp ");
    Serial.print(set_temp);
    //
    digitalWrite(RelayPin, HIGH);
    delay(1000);
    digitalWrite(RelayPin, LOW);
    
    



 }
 else {
  //Serial.print("relay flag OFF");
  digitalWrite(RelayPin, LOW);
 }

  delay(500);


}

/*
  SerialEvent occurs whenever a new data comes in the hardware serial RX. This
  routine is run between each time loop() runs, so using delay inside loop can
  delay response. Multiple bytes of data may be available.
*/
void serialEvent() {
  char endMarker = '\n';
  static byte ndx = 0;
  char rc;

    while (Serial.available() > 0) {
      rc = Serial.read();

       
      if (rc != endMarker) {
        receivedChars[ndx] = rc;
        ndx++;
        if (ndx >= numChars) {
          ndx = numChars - 1;
         }
      }
      else {
        receivedChars[ndx] = '\0'; // terminate the string
        ndx = 0;
        
      }
      new_data = true;
    }

    if (new_data){
      Serial.print("parseing");  
      delay(10);
      parseData();
      new_data= false;
    } 


    // }
}


//============

void parseData() {      // split the data into its parts

    char * strtokIndx; // this is used by strtok() as an index
    char com[5] = {0};
    strtokIndx = strtok(receivedChars,",");      // get the first part - the string
    strcpy(com, strtokIndx); // copy it to messageFromPC
    String command = String(com);
    Serial.print(command);  

    if (command =="ON"){

      start_relay_Flag = true;
      Serial.print("Relay true");  

    }

    else if (command=="OFF"){
      start_relay_Flag = false;

    }

    else if (command =="SET") {
      strtokIndx = strtok(NULL, ","); // this continues where the previous call left off
      ramp_set = atoi(strtokIndx);     // convert this part to an integer
      Serial.print(ramp_set);  
      
      strtokIndx = strtok(NULL, ",");
      set_temp = atof(strtokIndx);     // convert this part to a float
      Serial.print(set_temp);  

      start_relay_Flag = true;

    }

    else if (command =='temp') {
      
      strtokIndx = strtok(NULL, ",");
      actual_temp = atof(strtokIndx);     // convert this part to a float

      Serial.print(actual_temp);

      if (actual_temp >= set_temp-0.5 && actual_temp <= set_temp+0.5){
        start_relay_Flag = false;

      }
    }

    else {
      Serial.print("Wrong Data");
    }

    

}
