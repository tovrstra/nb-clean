"""Tests for nb_clean.clean_notebook."""

import nbformat

import nb_clean


def test_clean_notebook(
    dirty_notebook: nbformat.NotebookNode,
    clean_notebook: nbformat.NotebookNode,
) -> None:
    """Test nb_clean.clean_notebook."""
    assert nb_clean.clean_notebook(dirty_notebook) == clean_notebook


def test_clean_notebook_with_version(
    dirty_notebook_with_version: nbformat.NotebookNode,
    clean_notebook: nbformat.NotebookNode,
) -> None:
    """Test nb_clean.clean_notebook with language_info version."""
    assert (
        nb_clean.clean_notebook(dirty_notebook_with_version) == clean_notebook
    )


def test_clean_notebook_remove_empty_cells(
    clean_notebook_with_empty_cells: nbformat.NotebookNode,
    clean_notebook_without_empty_cells: nbformat.NotebookNode,
) -> None:
    """Test nb_clean.clean_notebook when removing empty cells."""
    assert (
        nb_clean.clean_notebook(
            clean_notebook_with_empty_cells, remove_empty_cells=True
        )
        == clean_notebook_without_empty_cells
    )


def test_clean_notebook_preserve_metadata(
    dirty_notebook: nbformat.NotebookNode,
    clean_notebook_with_metadata: nbformat.NotebookNode,
) -> None:
    """Test nb_clean.clean_notebook when preserving cell metadata."""
    assert (
        nb_clean.clean_notebook(dirty_notebook, preserve_cell_metadata=True)
        == clean_notebook_with_metadata
    )


def test_clean_notebook_preserve_outputs(
    dirty_notebook: nbformat.NotebookNode,
    clean_notebook_with_outputs: nbformat.NotebookNode,
) -> None:
    """Test nb_clean.clean_notebook when preserving cell outputs."""
    assert (
        nb_clean.clean_notebook(dirty_notebook, preserve_cell_outputs=True)
        == clean_notebook_with_outputs
    )
