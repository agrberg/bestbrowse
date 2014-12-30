class AddBaseUrlToVisits < ActiveRecord::Migration
  def change
    add_column :visits, :base_url, :string
  end
end
