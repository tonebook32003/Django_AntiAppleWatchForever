var hash = window.location.hash;
var changed = false;
if (hash.includes("tgWebAppPlatform=weba")) {
    hash = hash.replaceAll("tgWebAppPlatform = weba", "tgWebAppPlatform = android");
    changed = true;
} else if (hash.includes("tgWebAppPlatform = web")) {
    hash = hash.replaceAll("tgWebAppPlatform = web", "tgWebAppPlatform = android");
    changed = true;
}

window.location.hash = hash;
window.location.reload();
if (changed) {
    console.log("Reload page successfully");
} else {
    console.log("Reload page unsuccessfully");
}
