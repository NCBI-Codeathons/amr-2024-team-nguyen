# Load necessary libraries
library(ggplot2)

# Load the TSV file into a data frame
# Replace 'your_file.tsv' with your actual file path
data <- read.csv('element_stats.denovo.1per_genomes.10-90per_pl.tsv', sep = '\t', header = TRUE)

# Create the histogram using ggplot2
plot <- ggplot(data, aes(x = pl_call_perc)) +
  geom_histogram(bins = 100, fill = 'blue', color = 'black') +
  labs(title = 'Elems found in > 1% of genomes',
       x = 'Percentage of contigs that are Plasmids', 
       y = 'Number of AMR Elements') +
  scale_x_continuous(minor_breaks = seq(0, 100, by = 10)) +  # Set minor tick marks every 10 percentage points
  theme_minimal() +
  theme(panel.grid.minor.x = element_line(color = "gray", linetype = "dotted"),  # Style the minor grid lines
        text = element_text(size = 20),  # Increase overall font size
        axis.title = element_text(size = 18),  # Increase font size of axis titles
        axis.text = element_text(size = 18),   # Increase font size of axis tick labels
        plot.title = element_text(size = 28, face = "bold"))  # Increase font size for plot title

ggsave("output_plot.png", plot = plot, width = 8, height = 6, dpi = 300)
