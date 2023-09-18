import React from "react";

function Test(data) {
    const mapData = {
        "deviceData":[
            {
                "name":"iPad Pro",
                "RAM":6,
                "HomeButton":false,
                "TouchID":"No",
                "FaceID":"Yes"
            }, {
                "name":"iPhone Xs",
                "RAM":4,
                "HomeButton":false,
                "TouchID":"No",
                "FaceID":"Yes"
            }
        ]
    }

    return(
        <div>
            mapData.deviceData.map((appleDevice)=>{
                console.log(JSON.stringify(appleDevice))

                return(
                    <div>
                        기종: {appleDevice.name}<br></br>
                        렘:
                    </div>
                )
            })
        </div>
    )
};

export default Test;