# Merge Coplanar Mesh Faces in Rhino3D

Simplify and clean up mesh geometry by automatically merging adjacent coplanar faces into single n-gons. This custom Rhino script is designed to optimise mesh quality and readability, particularly useful when working with triangulated or imported geometries.

## What Does the Script Do?

The **Merge Coplanar Mesh Faces** command allows you to:

* Select multiple mesh objects in the viewport.
* Combine them into a single mesh and fully weld them.
* Automatically detect and merge adjacent coplanar faces into clean n-gons based on a user-defined angle tolerance.

This process is especially helpful for reducing face complexity after import, retopologising geometry, or preparing meshes for clean presentation or fabrication.

> **Note**: Requires **Rhino 7** or later (due to `AddPlanarNgons()` support).

## Why Use This Tool?

Rhino’s native tools do not provide an easy way to merge coplanar faces into n-gons. Triangulated or fragmented meshes can be difficult to work with, both visually and structurally. This script:

* Reduces mesh face count and improves legibility.
* Simplifies post-processing workflows.
* Helps with 3D printing and export to external software (e.g., Unreal, Blender, or Revit).

## How to Use the Script

### Load the Script in Rhino

**Method 1**:

1. Type `_RunPythonScript` in the command line.
2. Browse to the saved location of the script file and run it.

### Method 2 Creating a Button or Alias for Easy Access (Optional)

#### Creating a Toolbar Button

1. **Right-click** an empty area of a toolbar and select **New Button**.
2. In the **Button Editor**:

   * **Left Button Command**:

     ```plaintext
     ! _-RunPythonScript "FullPathToYourScript\merge_coplanar_mesh_faces.py"
     ```

     Replace `FullPathToYourScript` with the actual script file path.
   * **Tooltip**: For example, `Merge coplanar mesh faces into n-gons`.
   * **Icon (Optional)**: Assign a custom icon if desired.

#### Creating an Alias

1. Open **Tools > Options**, then go to the **Aliases** tab.
2. **Create a New Alias**:

   * **Alias**: e.g., `meshmerge`
   * **Command Macro**:

     ```plaintext
     _-RunPythonScript "FullPathToYourScript\merge_coplanar_mesh_faces.py"
     ```

### Using the Command

1. **Select** one or more mesh objects when prompted.
2. Enter an **angle tolerance** in degrees. Adjacent faces within this angle will be considered coplanar.
3. The script will:

   * Combine all selected meshes.
   * Fully weld them at 180°.
   * Merge coplanar faces using `AddPlanarNgons`.
   * Replace the original meshes with a new optimised version.

### Example Use Cases

* Cleaning up triangulated meshes from STL or OBJ imports.
* Preparing meshes for CNC or laser cutting.
* Reducing geometry complexity for viewport performance or mesh UV mapping.
