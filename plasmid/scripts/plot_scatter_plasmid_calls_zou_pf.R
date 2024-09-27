# Load necessary libraries
library(ggplot2)
library(plotly)

# Load the TSV file into a data frame
# Replace 'your_file.tsv' with your actual file path
data <- read.table("merge_clean_join_zou_pf_pred.denovo.tsv", quote="\"", comment.char="")

# Create the histogram using ggplot2
plot <- ggplot(data, aes(x = V5, y = V9, color = V4, genome=V2, contig=V1)) +
     geom_point() +
     labs(title="Plasmid Scores: Zou vs PF",
          x = 'Zou Plasmid Score',
	  y = 'PlasmidFinder Score',
	  color = 'Zou Call') +  # Add axis labels and legend title
     scale_color_manual(values = c("CH" = "blue", "PL" = "red")) +  # Set specific colors for "CH" and "PL"
     theme_minimal() +  # Use a minimal theme for a clean look
     theme(text = element_text(size = 20),
        axis.title = element_text(size = 18),  # Increase font size of axis titles
        axis.text = element_text(size = 18),   # Increase font size of axis tick labels
        plot.title = element_text(size = 20, face = "bold"))  # Increase font size for plot title
 

ggsave("merge_clean_join_zou_pf_pred.denovo.png", plot = plot, width = 8, height = 6, dpi = 300)

# convert to interactive
interactive_plot <- ggplotly(plot)

# Save the interactive plot as an HTML file
htmlwidgets::saveWidget(interactive_plot, "merge_clean_join_zou_pf_pred.denovo.html")