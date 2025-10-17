import React from "react";
import profilePic from "../assets/profile.jpg";

function Home() {
  return (
    <section id="home">
      <img src={profilePic} alt="Profile" className="profile-pic" />
      <h2>Hello, I'm Mthulisi Zulu</h2>
      <p>Welcome to my portfolio. I build web apps and cloud solutions.</p>
    </section>
  );
}

export default Home;
