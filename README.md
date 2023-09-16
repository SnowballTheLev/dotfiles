<h1>i3 Configuration</h1>

<p>This repository contains configuration files for the i3 tiling window manager on Debian GNU/Linux 12 (bookworm). The configuration is not intended to provide a productive or efficient window management experience. It represents my work-in-progress customization.</p>

<h2>Features</h2>

<ul>
  <li>Keyboard-driven window management for a fast and efficient workflow.</li>
  <li>Custom keybindings for various actions like launching applications, changing workspaces, and more.</li>
  <li>Integration with <code>picom</code> for desktop effects and transparency.</li>
  <li>System power management options like logout, reboot, shutdown, and locking.</li>
</ul>

<h2>Prerequisites</h2>

<ul>
  <li><a href="https://i3wm.org/">i3wm</a></li>
  <li><a href="https://github.com/yshui/picom">picom</a></li>
  <li><a href="https://github.com/jceb/dex">dex</a> (used for autostarting applications)</li>
  <li>Other utilities specified in the configuration file (e.g., <code>i3lock</code>, <code>xss-lock</code>, <code>feh</code>, <code>lxpolkit</code>, etc.)</li>
</ul>

<h2>Installation</h2>

<ol>
  <li>Clone this repository to your preferred location:</li>
</ol>

<pre><code>git clone https://github.com/SnowballTheLev/i3-config.git
mv /path/to/i3-config/i3/* $HOME/.config/i3/
</code></pre>

<ol start="2">
  <li>Review the <code>config</code> file and make any necessary customizations.</li>
  <li>Make sure you have the required utilities installed.</li>
  <li>Launch the i3 window manager:</li>
</ol>

<pre><code>i3
</code></pre>

<h2>Keybindings</h2>

<ul>
  <li>Modify and customize keybindings in the <code>config</code> file to match your preferences.</li>
  <li>The default <code>$mod</code> key is set to <code>Mod4</code> (Super key).</li>
</ul>

<h2>Customization</h2>

<ul>
  <li>Adjust colors, fonts, and other visual settings by editing the configuration file.</li>
  <li>Add or modify startup applications in the <code>exec</code> commands.</li>
  <li>Customize layout and gaps according to your workspace needs.</li>
</ul>

<h2>Additional Information</h2>

<ul>
  <li>The configuration includes power management options (logout, reboot, shutdown, locking) bound to key combinations. These can be accessed in the mode "exit" (<code>$mod+Shift+e</code>).</li>
  <li>Desktop effects and transparency are managed using <code>picom</code>. You can customize its behavior in the configuration.</li>
  <li>The <code>i3bar</code> is disabled and used <a href="https://github.com/brndnmtthws/conky">conky</a> with fork of <a href="https://github.com/SnowballTheLev/MinimalistConky">MinimalistConky</a> configuration instead.</li>
</ul>

<h2>Credits</h2>

<ul>
  <li>Alternating Layout used in this configuration is sourced from <a href="https://github.com/olemartinorg/i3-alternating-layout">i3-alternating-layout</a>.</li>
  <li><a href="https://github.com/SnowballTheLev/MinimalistConky">MinimalistConky</a> is inspired by <a href="https://github.com/dylanaraps/neofetch">neofetch</a> and <a href="https://www.opencode.net/deny26/minimalis-conky-2">Minimalis Conky 2</a>.</li>
</ul>

<h2>License</h2>

<p>This project is licensed under the <a href="GPL-LICENSE">GNU General Public License</a>.</p>
