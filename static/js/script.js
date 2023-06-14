const submit_button = document.querySelector('.function .submit');

document.querySelectorAll(".drag-zone-input").forEach(input_element => {
    const drag_zone_element = input_element.closest(".drag-zone");
    const drag_zone_text_element = drag_zone_element.querySelector(".drag-zone-text");
    const drag_zone_file_element = drag_zone_element.querySelector(".drag-zone-file");

    drag_zone_element.querySelector(".drag-zone-button").onclick = () => {
        input_element.click();
    };

    input_element.onchange = e => {
        if (e.target.files|length > 0) {
            drag_zone_file_element.textContent = "已選擇： " + e.target.files[0].name;
        }
    };

    drag_zone_element.addEventListener("dragover", e => {
        e.preventDefault();
        drag_zone_element.classList.add("drag-zone-hover");
        drag_zone_text_element.textContent = "放開以上傳檔案";
    });

    ["dragleave", "dragend"].forEach(type => {
        drag_zone_element.addEventListener(type, e => {
            drag_zone_element.classList.remove("drag-zone-hover");
            drag_zone_text_element.textContent = "拖曳檔案至此處";
        });
    });

    drag_zone_element.addEventListener("drop", e => {
        e.preventDefault();
        
        if (e.dataTransfer.files.length > 0){
            input_element.files = e.dataTransfer.files;
            drag_zone_file_element.textContent = "已選擇： " + e.dataTransfer.files[0].name;
            submit_button.click();
        }

        drag_zone_element.classList.remove("drag-zone-hover");
        drag_zone_text_element.textContent = "拖曳檔案至此處";
    });
});