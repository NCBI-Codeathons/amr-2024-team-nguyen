#!/usr/bin/env Rscript

# Load necessary libraries
library(ggplot2)
library(plotly)


# ----------------------------------------------------------------------
# BOTH called (join)
# ----------------------------------------------------------------------

# Load the TSV file into a data frame
# Replace 'your_file.tsv' with your actual file path
data <- read.table("merge_clean_join_zou_pf_pred.denovo.both.tsv", quote="\"", comment.char="")

# Create the histogram using ggplot2
plot <- ggplot(data, aes(x = V5, y = V7, color = V4, genome=V1, contig=V2)) +
     geom_point() +
     labs(title="Plasmid Scores: Zou vs PF\n(contigs both called)",
          x = 'Zou Plasmid Score',
	  y = 'PlasmidFinder Score',
	  color = 'Zou Call') +  # Add axis labels and legend title
     scale_color_manual(values = c("CH" = "blue", "PL" = "red")) +  # Set specific colors for "CH" and "PL"
     theme_minimal() +  # Use a minimal theme for a clean look
     theme(text = element_text(size = 20),
        axis.title = element_text(size = 18),  # Increase font size of axis titles
        axis.text = element_text(size = 18),   # Increase font size of axis tick labels
        plot.title = element_text(size = 20, face = "bold"))  # Increase font size for plot title
 

ggsave("merge_clean_join_zou_pf_pred.denovo.both.png", plot = plot, width = 8, height = 6, dpi = 300)

# convert to interactive
interactive_plot <- ggplotly(plot)

# Save the interactive plot as an HTML file
htmlwidgets::saveWidget(interactive_plot, "merge_clean_join_zou_pf_pred.denovo.both.html")

# ----------------------------------------------------------------------
# ALL CONTIGS called (outer left join)
# ----------------------------------------------------------------------

# Load the TSV file into a data frame
# Replace 'your_file.tsv' with your actual file path
data <- read.table("merge_clean_join_zou_pf_pred.denovo.all.tsv", quote="\"", comment.char="")

# Create the histogram using ggplot2
plot <- ggplot(data, aes(x = V5, y = V7, color = V4, genome=V1, contig=V2)) +
     geom_point() +
     labs(title="Plasmid Scores: Zou vs PF\n(all contigs)",
          x = 'Zou Plasmid Score',
	  y = 'PlasmidFinder Score',
	  color = 'Zou Call') +  # Add axis labels and legend title
     scale_color_manual(values = c("CH" = "blue", "PL" = "red")) +  # Set specific colors for "CH" and "PL"
     theme_minimal() +  # Use a minimal theme for a clean look
     theme(text = element_text(size = 20),
        axis.title = element_text(size = 18),  # Increase font size of axis titles
        axis.text = element_text(size = 18),   # Increase font size of axis tick labels
        plot.title = element_text(size = 20, face = "bold"))  # Increase font size for plot title
 

ggsave("merge_clean_join_zou_pf_pred.denovo.all.png", plot = plot, width = 8, height = 6, dpi = 300)

# convert to interactive
interactive_plot <- ggplotly(plot)

# Save the interactive plot as an HTML file
htmlwidgets::saveWidget(interactive_plot, "merge_clean_join_zou_pf_pred.denovo.all.html")