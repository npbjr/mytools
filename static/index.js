class App {
    
    constructor(document){
        this.document = document;
        this.onDocumentReady();
        // this.document.addEventListener('DOMContentLoaded', ()=>{
            
        // });  
    }
    text = "Please input your video url below";
    index = 0;
    runTextAnimation = () =>{
        if (this.index < this.text.length) {
            this.document.getElementById("message").innerHTML += this.text.charAt(this.index);
            this.index++;
            setTimeout(this.runTextAnimation, 50); 
        }
        else{
          setTimeout(() => {
                this.document.getElementById("message").innerHTML = ""; 
                this.index = 0; 
                this.runTextAnimation();
            }, 1000); 
        }
    }

    setUpButtonEvent(socket, iosession_key) {
        console.log(socket);
        const download_button = $('#download_video');
        const progress_container = $('.progress');
        const progress_bar = $('.progress-bar');

        progress_container.attr('hidden',true);

        const modalElement = document.getElementById('exampleModal');
        const modal = new bootstrap.Modal(modalElement);
        

        download_button.on('click', (event) => {
            
            event.preventDefault(); // Prevent default form submission
            progress_bar.attr('aria-valuenow', 0).css('width','0%');
            const videoUrl = document.getElementById('youtube_url').value;
            if(videoUrl == ""){
                alert('url is invalid')
                download_button.removeAttr("disabled");
                return false;
            }

            console.log("emiting download");
            progress_container.attr('hidden',false);

            progress_bar.attr('aria-valuenow', '1').css('width','1%');
            download_button.attr("disabled", "disabled");
            console.log("emiting download");

            var data = {
                link : videoUrl
            }
            downloadFile();
            function downloadFile() {
                fetch("/api/uploadvideo", {
                    method: 'POST',
                    headers: {
                        'IOSession-key': iosession_key,
                        'Authorization':'sample',
                        'Content-Type': 'application/json' // Specify the content type
                    },
                    body: JSON.stringify(data) // Convert the data to JSON
                })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.blob(); // Convert response to Blob
                })
                .then(blob => {
                    const url = window.URL.createObjectURL(blob); // Create a URL for the Blob
                    const a = document.createElement('a'); // Create an anchor element
                    a.href = url;
                    a.download = ''; // Set the file name for download
                    document.body.appendChild(a); // Append anchor to body
                    a.click(); // Programmatically click the anchor to trigger download
                    a.remove(); // Remove the anchor from the document
                    window.URL.revokeObjectURL(url); // Clean up the URL object
                })
                .catch(error => {
                    console.error('Error:', error);
                });
            }
            
            
            // socket.emit('download_video', { link: videoUrl, auth_key: "sample" });

        });

        socket.on('download_progress', function(data) {
            console.log("download progress "+data.progress)
            progress_container.attr('hidden',false);
            
            progress_bar.attr('aria-valuenow', data.progress).css('width',data.progress+'%');
        });

        socket.on('download_complete', function(data) {
            // alert(data.message);
            console.log(data);
            console.log('download success')
            progress_bar.attr('aria-valuenow', 100).css('width','100%');
            
            modal.show();
            setTimeout(() => {
                progress_bar.attr('aria-valuenow', 0).css('width','0%');
                progress_container.attr('hidden',true);
            }, 100); 
            setTimeout(()=>{
                modal.hide();   
                download_button.removeAttr("disabled")
            },3000)
        });
    
    }

    onDocumentReady() {
        this.runTextAnimation();
        fetch('/get_key')
        .then(response => response.json())
        .then(data => {
            const key = data.key;  
            const socket = io(key); 
                
            this.setUpButtonEvent(socket, key);
        })
        .catch(error => {
            console.error('Error fetching key:', error);
        });
        
    }
    
}

$(document).ready(()=> {
    new App(document);
});

