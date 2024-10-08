from typing import Optional
from wildlife_tracker.migration_tracking.migration import Migration, MigrationPath
from wildlife_tracker.habitat_management.habitat import Habitat


class MigrationManager:
    def __init__(self) -> None:
        self.migrations: dict[int, Migration] = {}
        self.paths: dict[int, MigrationPath] = {}
    
    def create_migration_path(self, species: str, start_location: Habitat, destination: Habitat, duration: Optional[int] = None) -> MigrationPath:
        path_id = len(self.paths) + 1
        path = MigrationPath(path_id, species, start_location, destination, duration)
        self.paths[path_id] = path
        return path
    
    def schedule_migration(self, migration_path: MigrationPath) -> None:
        migration_id = len(self.migrations) + 1
        migration = Migration(migration_id, migration_path)
        self.migrations[migration_id] = migration
    
    def remove_migration(self, migration_id: int) -> None:
        if migration_id in self.migrations:
            del self.migrations[migration_id]