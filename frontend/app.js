<script>
async function uploadFile() {
    const fileInput = document.getElementById("file");
    const file = fileInput.files[0];

    const formData = new FormData();
    formData.append("file", file);

    const response = await fetch("http://127.0.0.1:8000/upload/", {
        method: "POST",
        body: formData
    });

    const data = await response.json();
    console.log(data);

    document.getElementById("result").innerText =
        "Summary:\n" + data.summary + "\n\nAction Points:\n" + data.action_points;
}
</script>