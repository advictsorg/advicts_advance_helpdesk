/* @odoo-module */
//
// This file is meant to regroup your javascript code. You can either copy/past
// any code that should be executed on each page loading or write your own
// taking advantage of the Odoo framework to create new behaviors or modify
// existing ones. For example, doing this will greet any visitor with a 'Hello,
// world !' message in a popup:
//
/*
import { ConfirmationDialog } from '@web/core/confirmation_dialog/confirmation_dialog';
import publicWidget from '@web/legacy/js/public/public_widget';

publicWidget.registry.HelloWorldPopup = publicWidget.Widget.extend({
    selector: '#wrapwrap',

    init() {
        this.dialog = this.bindService("dialog");
    },
    start() {
        this.dialog.add(ConfirmationDialog, { body: 'Hello World' });
        return this._super.apply(this, arguments);
    },
});
*/
try {
  const dropZone = document.getElementById("drop-zone");
  const fileInput = document.getElementById("portal_file");
  const filePreview = document.getElementById("file-preview");
  let selectedFiles = [];

  dropZone.addEventListener("click", () => fileInput.click());

  fileInput.addEventListener("change", (event) => {
    handleFiles(event.target.files);
  });

  dropZone.addEventListener("dragover", (event) => {
    event.preventDefault();
    dropZone.classList.add("hover");
  });

  dropZone.addEventListener("dragleave", () => {
    dropZone.classList.remove("hover");
  });

  dropZone.addEventListener("drop", (event) => {
    event.preventDefault();
    dropZone.classList.remove("hover");
    handleFiles(event.dataTransfer.files);
  });

  function handleFiles(files) {
    for (let file of files) {
      if (!selectedFiles.some((f) => f.name === file.name)) {
        selectedFiles.push(file);
        displayFile(file);
      }
    }
    fileInput.files = createFileList(selectedFiles);
  }

  function displayFile(file) {
    const fileItem = document.createElement("div");
    fileItem.classList.add("file-item");

    const fileIcon = document.createElement("span");
    fileIcon.classList.add("file-icon");
    fileIcon.innerHTML = "📄";
    const fileName = document.createElement("span");
    fileName.classList.add("file-name");
    fileName.textContent = file.name;

    const removeBtn = document.createElement("span");
    removeBtn.classList.add("remove-file");
    removeBtn.innerHTML = "&times;";
    removeBtn.addEventListener("click", () => {
      removeFile(file.name);
    });

    fileItem.appendChild(fileIcon);
    fileItem.appendChild(fileName);
    fileItem.appendChild(removeBtn);
    filePreview.appendChild(fileItem);
  }

  function removeFile(fileName) {
    selectedFiles = selectedFiles.filter((file) => file.name !== fileName);
    fileInput.files = createFileList(selectedFiles);
    updatePreview();
  }

  function updatePreview() {
    filePreview.innerHTML = "";
    selectedFiles.forEach(displayFile);
  }

  function createFileList(files) {
    const dataTransfer = new DataTransfer();
    files.forEach((file) => dataTransfer.items.add(file));
    return dataTransfer.files;
  }
} catch (err) {}
