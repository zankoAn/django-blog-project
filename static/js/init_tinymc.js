window.djangoFileBrowser = (callback, value, meta) => {
		let fbURL = "filebrowser/browse/?pop=5&type=image";
console.log(fbURL);
    tinyMCE.activeEditor.windowManager.openUrl({
        title: "Filebrowser image/media/file picker",
        url: fbURL,
        width: 850,
        height: 500,
        onMessage: function (dialogApi, details) {
            callback(details.content);
            dialogApi.close();
        }
    });
    return false;
};
