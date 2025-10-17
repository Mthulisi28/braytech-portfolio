import React from "react";
import ProjectCard from "../components/ProjectCard";

const projects = [
  { title: "Portfolio Website", description: "Built with React + Vite" },
  { title: "Serverless Pipeline", description: "AWS S3 + Lambda project" },
];

function Projects() {
  return (
    <section id="projects">
      <h2>Projects</h2>
      <div className="projects-grid">
        {projects.map((p, index) => (
          <ProjectCard key={index} project={p} />
        ))}
      </div>
    </section>
  );
}

export default Projects;
