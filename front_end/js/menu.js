// Sample menu items array
const menuItems = [
    { title: "Meeting your Colleagues", description: "6 Video - 40 min", iconText: "Team Building" },
    { title: "Introduction to the Company", description: "5 Video - 30 min", iconText: "Overview" },
    { title: "Project Management Basics", description: "4 Video - 50 min", iconText: "Workflow" }
  ];
  
  // Function to create a card for each menu item
  function createCard(item) {
    // Create card container
    const card = document.createElement("div");
    card.classList.add("card");
  
    // Add image section with a save button
    const imgDiv = document.createElement("div");
    imgDiv.classList.add("img");
    const saveDiv = document.createElement("div");
    saveDiv.classList.add("save");
    const saveSvg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    saveSvg.setAttribute("class", "svg");
    saveSvg.setAttribute("width", "683");
    saveSvg.setAttribute("height", "683");
    saveSvg.setAttribute("viewBox", "0 0 683 683");
    saveSvg.setAttribute("fill", "none");
    saveSvg.innerHTML = `
      <g clip-path="url(#clip0)">
        <path d="M148.535 19.9999C137.179 19.9999 126.256 24.5092 118.223 32.5532C110.188 40.5866 105.689 51.4799 105.689 62.8439V633.382C105.689 649.556 118.757 662.667 134.931 662.667H135.039C143.715 662.667 151.961 659.218 158.067 653.09C186.451 624.728 270.212 540.966 304.809 506.434C314.449 496.741 327.623 491.289 341.335 491.289C355.045 491.289 368.22 496.741 377.859 506.434C412.563 541.074 496.752 625.242 524.816 653.348C530.813 659.314 538.845 662.667 547.308 662.667C563.697 662.667 576.979 649.395 576.979 633.019V62.8439C576.979 51.4799 572.48 40.5866 564.447 32.5532C556.412 24.5092 545.489 19.9999 534.133 19.9999H148.535Z" stroke="#CED8DE" stroke-width="40"></path>
      </g>
    `;
    saveDiv.appendChild(saveSvg);
    imgDiv.appendChild(saveDiv);
  
    // Add text section
    const textDiv = document.createElement("div");
    textDiv.classList.add("text");
    const title = document.createElement("p");
    title.classList.add("h3");
    title.textContent = item.title;
    const description = document.createElement("p");
    description.classList.add("p");
    description.textContent = item.description;
  
    // Add icon box
    const iconBox = document.createElement("div");
    iconBox.classList.add("icon-box");
    const iconSvg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    iconSvg.setAttribute("class", "svg");
    iconSvg.innerHTML = `
      <path style="fill:#3D6687;" d="M165,68.715l-26.327-26.327l37.363-37.363c3.739-3.739,9.801-3.739,13.54,0l12.786,12.786c3.739,3.739,3.739,9.801,0,13.54L165,68.715z"></path>
    `;
    const iconText = document.createElement("span");
    iconText.classList.add("span");
    iconText.textContent = item.iconText;
    iconBox.appendChild(iconSvg);
    iconBox.appendChild(iconText);
  
    textDiv.appendChild(title);
    textDiv.appendChild(description);
    textDiv.appendChild(iconBox);
  
    card.appendChild(imgDiv);
    card.appendChild(textDiv);
  
    return card;
  }
  
  // Append cards to the container
  const container = document.getElementById("menuContainer"); // Assuming you have a container with this ID
  menuItems.forEach(item => {
    const card = createCard(item);
    container.appendChild(card);
  });
  