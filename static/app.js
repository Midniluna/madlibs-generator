const storyNav = document.querySelector("#collapseTarget");
const hiddenStoryList = document.querySelector("table");

storyNav.addEventListener("mouseover", expandList);
storyNav.addEventListener("mouseout", collapseList);

function expandList() {
	console.log("you hovered!");
	hiddenStoryList.setAttribute("style", "visibility:visible;");
}

function collapseList() {
	console.log("Exited hovermode");
	hiddenStoryList.setAttribute("style", "visibility:hidden;");
}
